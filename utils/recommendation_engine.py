# utils/recommendation_engine.py

def suggest_alternative(clause):
    clause = clause.lower()

    if "terminate" in clause:
        return "Add a reasonable notice period and make termination mutual."

    if "liability" in clause:
        return "Cap liability to a fixed amount to reduce financial risk."

    if "non-compete" in clause:
        return "Reduce duration and limit geographic scope."

    if "confidentiality" in clause:
        return "Specify exceptions and confidentiality time period."

    return "Clause appears standard. No changes suggested."
