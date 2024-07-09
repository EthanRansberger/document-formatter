import os
import markdown
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from tkinter import Tk, filedialog
import pypandoc
from bs4 import BeautifulSoup

def markdown_to_html(markdown_text):
    return markdown.markdown(markdown_text)

def html_to_docx(html, docx_path):
    document = Document()
    soup = BeautifulSoup(html, 'html.parser')

    # Add title
    title = soup.find('h1')
    if title:
        run = document.add_heading(level=1).add_run(title.text)
        run.font.size = Pt(16)
        run.bold = True
        title.extract()

    # Add contact info
    contact_info = soup.find_all('p')[0:2]
    if contact_info:
        contact_paragraph = document.add_paragraph()
        contact_paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        for p in contact_info:
            run = contact_paragraph.add_run(p.text + '\n')
            run.font.size = Pt(12)
            run.bold = True
        contact_info[0].extract()
        contact_info[1].extract()

    # Add the rest of the content
    for element in soup.find_all(['h2', 'h3', 'p', 'ul']):
        if element.name == 'h2':
            heading = document.add_heading(level=2)
            run = heading.add_run(element.text)
            run.font.size = Pt(14)
            run.bold = True
        elif element.name == 'h3':
            heading = document.add_heading(level=3)
            run = heading.add_run(element.text)
            run.font.size = Pt(12)
            run.bold = True
        elif element.name == 'p':
            p = document.add_paragraph(element.text)
            p.paragraph_format.space_after = Pt(12)
        elif element.name == 'ul':
            for li in element.find_all('li'):
                document.add_paragraph(li.text, style='ListBullet')

    document.save(docx_path)

def docx_to_pdf(docx_path, pdf_path):
    output = pypandoc.convert_file(docx_path, 'pdf', outputfile=pdf_path)
    assert output == "", "Conversion error occurred"
    print(f"PDF file saved to {pdf_path}")

def select_file(title, filetypes):
    root = Tk()
    root.withdraw()  # Hide the root window
    initial_dir = os.path.dirname(os.path.abspath(__file__))  # Set default folder to script's location
    file_path = filedialog.askopenfilename(title=title, initialdir=initial_dir, filetypes=filetypes)
    return file_path

def save_file():
    root = Tk()
    root.withdraw()  # Hide the root window
    initial_dir = os.path.dirname(os.path.abspath(__file__))  # Set default folder to script's location
    file_path = filedialog.asksaveasfilename(title="Save DOCX file", initialdir=initial_dir, defaultextension=".docx", filetypes=[("Word files", "*.docx")])
    return file_path

# Main script
markdown_path = select_file("Select a Markdown file", [("Markdown files", "*.md")])
if markdown_path:
    with open(markdown_path, 'r', encoding='utf-8') as f:
        markdown_text = f.read()
    html_content = markdown_to_html(markdown_text)
    docx_path = save_file()
    if docx_path:
        html_to_docx(html_content, docx_path)
        print(f"DOCX file saved to {docx_path}")
        pdf_path = os.path.splitext(docx_path)[0] + '.pdf'
        docx_to_pdf(docx_path, pdf_path)
    else:
        print("Save operation cancelled.")
else:
    print("File selection cancelled.")
