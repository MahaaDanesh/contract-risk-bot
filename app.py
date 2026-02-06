import streamlit as st
from utils.text_extractor import extract_text
from utils.clause_splitter import split_clauses
from utils.llm_helper import classify_contract, explain_clause, assess_risk
from utils.recommendation_engine import suggest_alternative

st.set_page_config(page_title="Contract Risk Bot", layout="wide")

st.title("📄 Contract Analysis & Risk Assessment Bot")
st.caption("AI-powered contract understanding for SMEs")
st.warning("⚠️ This tool provides AI-assisted insights and is not legal advice.")

uploaded_file = st.file_uploader(
    "Upload Contract (PDF / DOCX / TXT)",
    type=["pdf", "docx", "txt"]
)

if uploaded_file:
    contract_text = extract_text(uploaded_file)

    if contract_text.strip():
        st.success("Text extracted successfully!")

        # Contract type
        st.subheader("📌 Contract Type")
        contract_type = classify_contract(contract_text)
        st.info(contract_type)

        # Clause analysis
        st.subheader("📑 Clause-by-Clause Analysis")
        clauses = split_clauses(contract_text)

        for i, clause in enumerate(clauses, start=1):
            risk = assess_risk(clause)
            emoji = {"High Risk": "🔴", "Medium Risk": "🟡", "Low Risk": "🟢"}[risk]

            with st.expander(f"{emoji} Clause {i} — {risk}"):
                st.write(clause)

                st.markdown("**🧠 Plain English Explanation**")
                st.write(explain_clause(clause))

                st.markdown("**🤝 Suggested Improvement**")
                st.success(suggest_alternative(clause))

    else:
        st.error("Failed to extract contract text.")
