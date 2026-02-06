from fpdf import FPDF
from datetime import datetime

class ContractPDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Contract Risk Assessment Report", ln=True, align="C")
        self.ln(5)

def generate_pdf(
    filename,
    contract_type,
    overall_level,
    risk_percentage,
    summary_text,
    high_risk_clauses
):
    pdf = ContractPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font("Arial", size=11)

    pdf.cell(0, 8, f"Generated on: {datetime.now().strftime('%d-%m-%Y %H:%M')}", ln=True)
    pdf.ln(5)

    pdf.set_font("Arial", "B", 11)
    pdf.cell(0, 8, "Contract Overview", ln=True)
    pdf.set_font("Arial", size=11)

    pdf.multi_cell(0, 8, f"""
Contract Type: {contract_type}
Overall Risk Level: {overall_level}
Risk Percentage: {risk_percentage}%
""")

    pdf.ln(3)
    pdf.set_font("Arial", "B", 11)
    pdf.cell(0, 8, "Business-Friendly Summary", ln=True)
    pdf.set_font("Arial", size=11)
    pdf.multi_cell(0, 8, summary_text)

    pdf.ln(3)
    pdf.set_font("Arial", "B", 11)
    pdf.cell(0, 8, "High Risk Clauses", ln=True)
    pdf.set_font("Arial", size=11)

    if high_risk_clauses:
        for c in high_risk_clauses:
            pdf.multi_cell(
                0,
                8,
                f"- Clause {c['clause_id']}: {c['reason']}"
            )
    else:
        pdf.multi_cell(0, 8, "No high-risk clauses detected.")

    pdf.ln(5)
    pdf.set_font("Arial", "I", 9)
    pdf.multi_cell(
        0,
        6,
        "Disclaimer: This report is generated using AI and is not a substitute "
        "for professional legal advice."
    )

    output_path = f"{filename}_Contract_Risk_Report.pdf"
    pdf.output(output_path)

    return output_path
