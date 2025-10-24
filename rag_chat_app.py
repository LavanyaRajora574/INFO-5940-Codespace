import os, tempfile
from typing import Dict, List, Tuple

import streamlit as st

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.documents import Document

from config import *
from document_helper import *


def doc_context(docs: List[Document]):
    lines = []
    for d in docs:
        src = d.metadata.get("source", "unknown")
        page = d.metadata.get("page", None)
        tag = f"{src}" if page is None else f"{src} (p.{page+1})"
        lines.append(f"[{tag}] {d.page_content}")
    return "\n\n".join(lines)

def fetch_response(question, chat_history, collection_name):
    embeddings = OpenAIEmbeddings(
        model=EMBED_MODEL,
        api_key=OPENAI_API_KEY,
        base_url=OPENAI_BASE_URL,
    )
    vs = Chroma(
        collection_name=collection_name,
        embedding_function=embeddings,
    )
    retriever = vs.as_retriever(search_type="mmr", k=TOP_K, fetch_k=FETCH_K)
    try:
        docs = retriever.invoke(question)
    except AttributeError:
        docs = retriever.get_relevant_documents(question)

    context = doc_context(docs)

    messages = [
        SystemMessage(content=LLM_PROMPT),
        SystemMessage(content=f"Context documents:\n\n{context}"),
    ]

    for turn in chat_history[-4:]:
        messages.append(HumanMessage(content=turn["user"]))
        messages.append(SystemMessage(content=f"Assistant (previous): {turn['assistant']}"))

    messages.append(HumanMessage(content=question))

    llm = ChatOpenAI(
        model=CHAT_MODEL,
        temperature=0.2,
        api_key=OPENAI_API_KEY,
        base_url=OPENAI_BASE_URL,
    )
    resp = llm.invoke(messages)
    return resp.content, docs

st.set_page_config(page_title="Document Chat", layout="wide")
st.title("Document Chat")

if "history" not in st.session_state:
    st.session_state.history = []

with st.sidebar:
    st.header("Documents")
    uploaded = st.file_uploader("Upload .txt/.md/.pdf", accept_multiple_files=True, type=["txt", 'md', "pdf"])
    if uploaded:
        with st.spinner("Indexing..."):
            tmp_paths = []
            for doc in uploaded:
                suffix = os.path.splitext(doc.name)[1].lower()
                with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
                    tmp.write(doc.read())
                    tmp_paths.append(tmp.name)

            docs = load(tmp_paths)
            chunks = chunk(docs)
            build(chunks, COLLECTION)
        st.info("Index Successful.")

for turn in st.session_state.history:
    with st.chat_message("user"):
        st.write(turn["user"])
    with st.chat_message("assistant"):
        st.write(turn["assistant"])

if prompt := st.chat_input("Ask about your documents…"):
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Thinking…"):
            answer, docs = fetch_response(prompt, st.session_state.history, COLLECTION)
            st.write(answer)
    st.session_state.history.append({"user": prompt, "assistant": answer})

