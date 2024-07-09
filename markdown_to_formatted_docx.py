import os
import json
import markdown
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from tkinter import Tk, filedialog
import pypandoc
from bs4 import BeautifulSoup

def load_formatting_config(config_path):
    with open(config_path, 'r') as f:
        return json.load(f)

def markdown_to_html(markdown_text):
    return markdown.markdown(markdown_text)

def html_to_docx(html, docx_path, formatting):
    document = Document()
    soup = BeautifulSoup(html, 'html.parser')

    # Add title
    title = soup.find('h1')
    if title:
        run = document.add_heading(level=1).add_run(title.text)
        run.font.size = Pt(formatting['title']['font_size'])
        run.bold = formatting['title']['bold']
        title.extract()

    # Add contact info
    contact_info = soup.find_all('p')[0:2]
    if contact_info:
        contact_paragraph = document.add_paragraph()
        contact_paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        for p in contact_info:
            run = contact_paragraph.add_run(p.text + '\n')
            run.font.size = Pt(formatting['contact_info']['font_size'])
            run.bold = formatting['contact_info']['bold']
        contact_info[0].extract()
        contact_info[1].extract()

    # Add the rest of the content
    for element in soup.find_all(['h2', 'h3', 'p', 'ul']):
        if element.name == 'h2':
            heading = document.add_heading(level=2)
            run = heading.add_run(element.text)
            run.font.size = Pt(formatting['heading1']['font_size'])
            run.bold = formatting['heading1']['bold']
        elif element.name == 'h3':
            heading = document.add_heading(level=3)
            run = heading.add_run(element.text)
            run.font.size = Pt(formatting['heading2']['font_size'])
            run.bold = formatting['heading2']['bold']
        elif element.name == 'p':
            p = document.add_paragraph(element.text)
            p.paragraph_format.space_after = Pt(formatting['paragraph']['space_after'])
            p.style.font.size = Pt(formatting['paragraph']['font_size'])
        elif element.name == 'ul':
            for li in element.find_all('li'):
                p = document.add_paragraph(li.text, style='ListBullet')
                p.style.font.size = Pt(formatting['paragraph']['font_size'])

    document.save(docx_path)

def docx_to_pdf(docx_path, pdf_path):
    output = pypandoc.convert_file(docx_path, 'pdf', outputfile=pdf_path, extra_args=['--pdf-engine=pdflatex'])
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
formatting_config_path = select_file("Select the JSON formatting configuration file", [("JSON files", "*.json")])
markdown_path = select_file("Select a Markdown file", [("Markdown files", "*.md")])

if markdown_path and formatting_config_path:
    with open(markdown_path, 'r', encoding='utf-8') as f:
        markdown_text = f.read()
    html_content = markdown_to_html(markdown_text)
    formatting = load_formatting_config(formatting_config_path)
    docx_path = save_file()
    if docx_path:
        html_to_docx(html_content, docx_path, formatting)
        print(f"DOCX file saved to {docx_path}")
        pdf_path = os.path.splitext(docx_path)[0] + '.pdf'
        docx_to_pdf(docx_path, pdf_path)
    else:
        print("Save operation cancelled.")
else:
    print("File selection cancelled.")
