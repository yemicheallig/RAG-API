from .file_loader import load_documents

def chunk_text(text, chunk_size=500, overlap=100):
    chunks = []
    start = 0
    
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
        
    return chunks

def process_documents():
    docs = load_documents()
    all_chunks = []
    
    for text in docs:

        chunks = chunk_text(text)

        for i, chunk in enumerate(chunks):

            all_chunks.append({
                "text": chunk,
                "source": "document",
                "chunk_id": i
            })

    return all_chunks