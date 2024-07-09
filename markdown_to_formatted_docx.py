import os
import json
import markdown
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from tkinter import Tk, filedialog
import pypandoc
from bs4 import BeautifulSoup

def load_formatting_config(config_path):
    with open(config_path, 'r') as f:
        return json.load(f)

def markdown_to_html(markdown_text):
    return markdown.markdown(markdown_text)

def get_formatting_value(formatting, section, key, default):
    return formatting.get(section, {}).get(key, default)

def html_to_docx(html, docx_path, formatting):
    document = Document()
    soup = BeautifulSoup(html, 'html.parser')

    # Add title
    title = soup.find('h1')
    if title:
        run = document.add_heading(level=1).add_run(title.text)
        run.font.size = Pt(get_formatting_value(formatting, 'title', 'font_size', 16))
        run.bold = get_formatting_value(formatting, 'title', 'bold', True)
        title.extract()

    # Add contact info
    contact_info = soup.find_all('p')[0:2]
    if contact_info:
        contact_paragraph = document.add_paragraph()
        contact_paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
        for p in contact_info:
            run = contact_paragraph.add_run(p.text + '\n')
            run.font.size = Pt(get_formatting_value(formatting, 'contact_info', 'font_size', 12))
            run.bold = get_formatting_value(formatting, 'contact_info', 'bold', True)
            run.italic = get_formatting_value(formatting, 'contact_info', 'italic', False)
            if 'color' in formatting.get('contact_info', {}):
                run.font.color.rgb = RGBColor.from_string(formatting['contact_info']['color'])
        contact_info[0].extract()
        contact_info[1].extract()

    # Add the rest of the content
    for element in soup.find_all(['h2', 'h3', 'p', 'ul']):
        if element.name == 'h2':
            heading = document.add_heading(level=2)
            run = heading.add_run(element.text)
            run.font.size = Pt(get_formatting_value(formatting, 'heading1', 'font_size', 14))
            run.bold = get_formatting_value(formatting, 'heading1', 'bold', True)
            run.italic = get_formatting_value(formatting, 'heading1', 'italic', False)
            if 'color' in formatting.get('heading1', {}):
                run.font.color.rgb = RGBColor.from_string(formatting['heading1']['color'])
        elif element.name == 'h3':
            heading = document.add_heading(level=3)
            run = heading.add_run(element.text)
            run.font.size = Pt(get_formatting_value(formatting, 'heading2', 'font_size', 12))
            run.bold = get_formatting_value(formatting, 'heading2', 'bold', False)
            run.italic = get_formatting_value(formatting, 'heading2', 'italic', False)
            if 'color' in formatting.get('heading2', {}):
                run.font.color.rgb = RGBColor.from_string(formatting['heading2']['color'])
        elif element.name == 'p':
            p = document.add_paragraph(element.text)
            p.paragraph_format.space_after = Pt(get_formatting_value(formatting, 'paragraph', 'space_after', 12))
            p.style.font.size = Pt(get_formatting_value(formatting, 'paragraph', 'font_size', 11))
            if 'color' in formatting.get('paragraph', {}):
                for run in p.runs:
                    run.font.color.rgb = RGBColor.from_string(formatting['paragraph']['color'])
        elif element.name == 'ul':
            for li in element.find_all('li'):
                p = document.add_paragraph(li.text, style='ListBullet')
                p.style.font.size = Pt(get_formatting_value(formatting, 'paragraph', 'font_size', 11))
                if 'color' in formatting.get('paragraph', {}):
                    for run in p.runs:
                        run.font.color.rgb = RGBColor.from_string(formatting['paragraph']['color'])

    document.save(docx_path)

def docx_to_pdf(docx_path, pdf_path):
    output = pypandoc.convert_file(docx_path, 'pdf', outputfile=pdf_path, extra_args=['--pdf-engine=pdflatex'])
    assert output == "", "Conversion error occurred"
    print(f"PDF file saved to {pdf_path}")

def select_files(title, filetypes):
    root = Tk()
    root.withdraw()  # Hide the root window
    initial_dir = os.path.dirname(os.path.abspath(__file__))  # Set default folder to script's location
    file_paths = filedialog.askopenfilenames(title=title, initialdir=initial_dir, filetypes=filetypes)
    return list(file_paths)

def create_output_folder():
    output_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    return output_folder

# Main script
formatting_config_paths = select_files("Select the JSON formatting configuration files", [("JSON files", "*.json")])
markdown_paths = select_files("Select the Markdown files", [("Markdown files", "*.md")])

if markdown_paths and formatting_config_paths:
    output_folder = create_output_folder()
    for markdown_path in markdown_paths:
        with open(markdown_path, 'r', encoding='utf-8') as f:
            markdown_text = f.read()
        html_content = markdown_to_html(markdown_text)
        for formatting_config_path in formatting_config_paths:
            formatting = load_formatting_config(formatting_config_path)
            base_filename = os.path.splitext(os.path.basename(markdown_path))[0]
            formatting_name = os.path.splitext(os.path.basename(formatting_config_path))[0]
            docx_filename = f"{base_filename}_{formatting_name}.docx"
            docx_path = os.path.join(output_folder, docx_filename)
            html_to_docx(html_content, docx_path, formatting)
            print(f"DOCX file saved to {docx_path}")
            pdf_filename = f"{base_filename}_{formatting_name}.pdf"
            pdf_path = os.path.join(output_folder, pdf_filename)
            docx_to_pdf(docx_path, pdf_path)
else:
    print("File selection cancelled.")
