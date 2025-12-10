import os
from dotenv import load_dotenv

load_dotenv()

# LLM(Groq) Config
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama-3.1-8b-instant"

# Embedding(HuggingFace) Config
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
PERSIST_DIR = "chroma_db"

# VectorDB(ChromaDB) Paths
ORIGINAL_CSV_PATH = "data/anime_with_synopsis.csv"
PROCESSED_CSV_PATH = "data/anime_updated.csv"