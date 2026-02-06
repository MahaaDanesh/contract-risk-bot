import re

RISK_KEYWORDS = {
    "High": [
        "indemnify", "penalty", "liquidated damages",
        "non-compete", "exclusive", "unilateral",
        "without cause", "irrevocable", "in perpetuity"
    ],
    "Medium": [
        "termination", "arbitration", "jurisdiction",
        "auto-renewal", "lock-in", "confidentiality",
        "intellectual property"
    ]
}

RISK_SCORES = {
    "Low": 1,
    "Medium": 2,
    "High": 3
}

def keyword_risk_analysis(text):
    text_lower = text.lower()

    for level, keywords in RISK_KEYWORDS.items():
        for kw in keywords:
            if re.search(rf"\b{kw}\b", text_lower):
                return level, f"Contains risky term: '{kw}'"

    return "Low", "No obvious risky terms detected"


def calculate_contract_risk(clause_results):
    total_score = sum(RISK_SCORES[c["risk_level"]] for c in clause_results)
    max_score = len(clause_results) * 3

    risk_percentage = round((total_score / max_score) * 100, 2)

    if risk_percentage >= 66:
        level = "HIGH"
    elif risk_percentage >= 33:
        level = "MEDIUM"
    else:
        level = "LOW"

    return risk_percentage, level
