# Overview:
This project is a Retrieval-Augmented Generation (RAG) app built with Streamlit and LangChain. It allows users to upload .txt, .md, and .pdf files (up to 200MB each) and ask questions about their content. The system automatically chunks documents, stores them in ChromaDB, and uses OpenAI models to generate context-grounded answers.

## Implementation

### 1. Model & Embeddings  
The application leverages **OpenAI models** for both text understanding and response generation.

- **Chat Model:** `openai.gpt-5-chat` — chosen for its speed and advanced contextual reasoning.
- **Embedding Model:** `openai.text-embedding-3-small` — used for faster processing of contextual information efficiently.

### 2. Frontend & Interaction  
Built with **Streamlit**, the app delivers an intuitive web-based interface.  
Streamlit handles user interactions and rendering, while backend logic and RAG pipeline operations are managed through helper functions.

### 3. Document Loading  
The app supports multiple document formats using **LangChain loaders**:
- `TextLoader` — for plain text files (`.txt`, `.md`, etc.)  
- `PyPDFLoader` — for parsing and chunking PDF documents

### 4. Vector Storage  
Document embeddings are stored and retrieved using **ChromaDB**.
This vector store is stored in memory and is lost when the application stops.

### 5. Chunking Strategy  
To improve retrieval accuracy and preserve contextual continuity, documents are divided using **LangChain’s `RecursiveCharacterTextSplitter`**.  
This ensures efficient query-time recall and semantic linkage between neighboring chunks.

- **Chunk Size:** `800` (based on best practices suggesting 800–1200)  
- **Overlap:** `80` (~10%) to maintain contextual smoothness between chunks

### 6. Configuration and Helper Methods
Added variables in `config.py` for API key, model names, chunk settings, and retrieval parameters. The API key is loaded from environment variable and is not exposed.
Document helper methods are exported from `document_helper.py` containing methods to load the documents and process them.

## Run Instructions:
Open the provided Codespace environment.
Install dependencies: pip install -r requirements.txt

### Run the app:
`OPENAI_API_KEY=<your-api-key> streamlit run rag_chat_app.py`

### Open the app:
Now open http://localhost:8501 in the browser. This will connect with the port 8501 and run the app in the browser.

## How It Works:
- Upload one or more .txt/.pdf/.md files in the sidebar.
- Once uploaded these documents will be processed automatically
- The app extracts and splits the text into smaller chunks using `RecursiveCharacterTextSplitter`.
- Chunks are embedded with `OpenAIEmbeddings` and stored in `ChromaDB`.
- When a question is asked, the retriever fetches relevant Vector Store and Chat with OpenAI to generate an answer based on them.
- The responses also consider previous questions and responses to build upon the context of the chat for a more natural conversation.

## Tools Used:
- Streamlit – for the chat interface
- LangChain – for document processing and RAG pipeline
- ChromaDB – for vector storage and retrieval
- OpenAI API – for embeddings and language generation
- Python Standard Libraries – for file handling
- GitHub Codespace – for development environment
