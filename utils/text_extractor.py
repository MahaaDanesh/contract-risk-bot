# utils/text_extractor.py

import docx
import PyPDF2

def extract_text(uploaded_file):
    if uploaded_file.name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")

    elif uploaded_file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(uploaded_file)
        return " ".join(page.extract_text() for page in reader.pages)

    elif uploaded_file.name.endswith(".docx"):
        doc = docx.Document(uploaded_file)
        return " ".join(p.text for p in doc.paragraphs)

    else:
        return ""
