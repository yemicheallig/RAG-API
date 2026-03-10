import os
from pypdf import PdfReader
from docx import Document

DATA_PATH = "data"

def load_txt(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def load_pdf(path):
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def load_docx(path):
    doc = Document(path)
    return "\n".join([para.text for para in doc.paragraphs])

def load_documents():
    documents = []

    for file in os.listdir(DATA_PATH):
        path = os.path.join(DATA_PATH, file)

        if file.endswith(".txt"):
            documents.append(load_txt(path))

        elif file.endswith(".pdf"):
            documents.append(load_pdf(path))

        elif file.endswith(".docx"):
            documents.append(load_docx(path))

    return documents