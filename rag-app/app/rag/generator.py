from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL = "llama-3.1-8b-instant"

def generate_answer(question, context_chunks):

    context = "\n\n---\n\n".join(context_chunks)
    prompt = f"""
You are a helpful assistant.

Answer the question ONLY using the provided context.
If the answer is not in the context, say "I don't know."

Context:   
{context}

Question:
{question}

Answer:
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content