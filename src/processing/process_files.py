from docx import Document
from fpdf import FPDF

def docx_to_pdf(docx_path, pdf_path):
    doc = Document(docx_path)
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    for para in doc.paragraphs:
        pdf.set_font("Arial", size=12)
        text = para.text.encode('latin-1', 'replace').decode('latin-1')
        pdf.multi_cell(0, 10, text)
    pdf.output(pdf_path)
    print(f"PDF file saved to {pdf_path}")

if __name__ == "__main__":
    # Example usage
    docx_path = "path/to/your/input.docx"
    pdf_path = "path/to/your/output.pdf"
    docx_to_pdf(docx_path, pdf_path)
