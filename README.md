Incase the API is not working for u, just create 'data' folder inside the rag-app using the folder structure below. Amd another disclaimer is that the project works without some files like DOKER and utils

# RAG Application (FastAPI + FAISS + Groq)

## Project Overview
This project implements a Retrieval-Augmented Generation (RAG) pipeline using FastAPI, FAISS, and an LLM API.

## Project Structure
```
rag-app/
│
├── app/
│   ├── main.py
│   └── rag/
│       ├── ingest.py
│       ├── file_loader.py
│       ├── vector_store.py
│       ├── query.py
│       ├── generator.py
│       ├── retriever.py
│       └── utils.py
│
├── data/
│   └── example.txt
│
├── faiss_index/
├── chunks.pkl
├── .env
├── requirements.txt
├── Dockerfile
└── README.md
```

## Pipeline Flow
```
data/
   ↓
ingest.py
   ↓
chunks
   ↓
vector_store.py
   ↓
FAISS index
   ↓
query.py
   ↓
generator.py
   ↓
FastAPI /ask endpoint
```

## How to Run
1. Install requirements
2. Add API key to .env
3. Run ingest
4. Start FastAPI server
