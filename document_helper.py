import os
from typing import List
from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from config import *

def load(paths: List[str]):
    docs = []
    for p in paths:
        ext = os.path.splitext(p)[1].lower()
        if ext == ".txt":
            docs.extend(TextLoader(p, encoding="utf-8").load())
        elif ext == ".pdf":
            docs.extend(PyPDFLoader(p).load())
        else:
            raise ValueError(f"Unsupported file type: {ext}")
    return docs

def chunk(docs):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        add_start_index=True,
        separators=["\n\n", "\n", " ", ""],
    )
    return splitter.split_documents(docs)

def build(chunks, collection_name):
    embeddings = OpenAIEmbeddings(
        model=EMBED_MODEL,
        api_key=OPENAI_API_KEY,
        base_url=OPENAI_BASE_URL,
    )
    vs = Chroma(
        collection_name=collection_name,
        embedding_function=embeddings,
    )
    vs.add_documents(chunks)
    vs.persist()
    return vs
