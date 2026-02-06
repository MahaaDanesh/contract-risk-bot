# utils/clause_splitter.py

def split_clauses(text):
    clauses = []
    for line in text.split("\n"):
        line = line.strip()
        if len(line) > 30:
            clauses.append(line)
    return clauses
