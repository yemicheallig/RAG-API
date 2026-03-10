from .vector_store import search
from .generator import generate_answer

def ask_question(question, index, chunks):

    results = search(question, index, chunks)

    context_chunks = [r["text"] for r in results]

    answer = generate_answer(question, context_chunks)

    return {
        "answer": answer,
        "sources": results
    }