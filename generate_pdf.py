from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

with open("identite_IA.txt", "r", encoding="utf-8") as f:
    for line in f:
        pdf.cell(0, 10, line.strip(), ln=True)

pdf.output("identite_IA.pdf")
print("PDF généré : identite_IA.pdf")
