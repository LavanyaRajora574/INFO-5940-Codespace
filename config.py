import os
from dotenv import load_dotenv

load_dotenv()

# Configuration parameters
EMBED_MODEL = "openai.text-embedding-3-small"
CHAT_MODEL  = "openai.gpt-5-chat"
CHUNK_SIZE = 800
CHUNK_OVERLAP = 80
TOP_K = 5
FETCH_K = 15
COLLECTION = "doc-rag"
PERSIST_DIR = ".chatdocs"

LLM_PROMPT = """You are a predessional assistant answering conciseely ONLY from the provided documents.
Say you don't have required information if the answer is not in the documents or no documents uploaded.
"""

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_BASE_URL  = os.getenv("OPENAI_BASE_URL", "https://api.ai.it.cornell.edu")