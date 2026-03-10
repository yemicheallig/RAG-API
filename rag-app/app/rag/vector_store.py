import faiss
import os
import pickle
from sentence_transformers import SentenceTransformer
import numpy as np

INDEX_PATH = "faiss_index"
CHUNKS_PATH = "chunks.pkl"

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def create_faiss_index(chunks):

    if len(chunks) == 0:
        raise ValueError("No chunks found. Please add documents to the data folder.")

    print("Creating embeddings...")

    embeddings = model.encode(chunks, show_progress_bar=True)
    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings) 

    return index, embeddings

def save_index(index, chunks):
    faiss.write_index(index, INDEX_PATH)

    with open(CHUNKS_PATH, "wb") as f:
        pickle.dump(chunks, f)

    print("Index saved successfully.")

def load_index():
    if not os.path.exists(INDEX_PATH):
        return None, None

    index = faiss.read_index(INDEX_PATH)

    with open(CHUNKS_PATH, "rb") as f:
        chunks = pickle.load(f)

    return index, chunks

def search(query, index, chunks, k=3):

    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")
    
    distances, indices = index.search(query_embedding, k)

    results = []

    for i, idx in enumerate(indices[0]):

        if idx == -1:
            continue

        chunk = chunks[idx]

        results.append({
            "text": chunk["text"],
            "source": chunk["source"],
            "score": float(distances[0][i])
        })
    
    results = sorted(results, key=lambda x: x["score"])

    return results
