# utils/llm_helper.py

def classify_contract(text):
    text = text.lower()
    if "employment" in text:
        return "Employment Agreement"
    elif "confidentiality" in text or "nda" in text:
        return "Non-Disclosure Agreement"
    elif "service" in text:
        return "Service Agreement"
    elif "lease" in text or "rent" in text:
        return "Lease Agreement"
    else:
        return "General Business Contract"


def explain_clause(clause):
    return "This clause defines legal responsibilities or restrictions for one or more parties."


def assess_risk(clause):
    clause = clause.lower()
    if any(word in clause for word in ["terminate", "liability", "penalty", "indemnity"]):
        return "High Risk"
    elif any(word in clause for word in ["confidentiality", "non-compete", "arbitration"]):
        return "Medium Risk"
    else:
        return "Low Risk"
