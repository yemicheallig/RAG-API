Incase the API is not working for u, just create 'data' folder inside the rag-app using the folder structure below. Amd another disclaimer is that the project works without some files like DOKER and utils
folder structure:
rag-app/
│
├── app/
│   │
│   ├── main.py                # FastAPI entry point
│   │
│   └── rag/
│       ├── __init__.py
│       ├── ingest.py          # Document processing & chunking
│       ├── file_loader.py     # Loads documents from /data
│       ├── vector_store.py    # FAISS index creation, saving, searching
│       ├── query.py           # RAG pipeline (retrieve + generate)
│       ├── generator.py       # LLM call (Groq / LLM prompt)
│       │
│       ├── retriever.py       # (optional / not necessary for this project)
│       └── utils.py           # (optional helper functions)
│
├── data/                      # Documents used for RAG
│   └── example.txt
│
├── faiss_index                # Saved FAISS index (generated automatically)
├── chunks.pkl                 # Stored chunks metadata
│
├── .env                       # API keys (Groq key)
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Container setup
│
└── README.md                  # How to run the project

project working pipeline:
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
