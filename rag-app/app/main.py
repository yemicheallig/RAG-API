from fastapi import FastAPI
from pydantic import BaseModel

from app.rag.ingest import process_documents
from app.rag.vector_store import create_faiss_index, save_index, load_index 
from app.rag.query import ask_question


app = FastAPI()

# Try loading existing index
index, chunks = load_index()

# If index doesn't exist, build it
if index is None:

    print("No index found. Creating new index...")

    chunks = process_documents()
    print(f"Total chunks: {len(chunks)}")

    index, embeddings = create_faiss_index(chunks)

    save_index(index, chunks)

class Question(BaseModel):
    question: str

# Health endpoint
@app.get("/")
def home():
    return {"message": "RAG API is running"}

# Ask endpoint
@app.post("/ask")
def ask(q: Question):

    result = ask_question(q.question, index, chunks)

    return result