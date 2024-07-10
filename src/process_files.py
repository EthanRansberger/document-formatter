import os
import json
from glob import glob
from markdown_to_formatted_docx import markdown_to_html, html_to_docx, load_formatting_config, create_output_folders, docx_to_pdf

# Define input and output directories
sample_md_dir = 'tests/samples/sample_md'
sample_json_dir = 'tests/samples/sample_json'
docx_output_folder, pdf_output_folder = create_output_folders()

# Get all markdown and JSON files
markdown_files = glob(os.path.join(sample_md_dir, '*.md'))
json_files = glob(os.path.join(sample_json_dir, '*.json'))

# Process each combination of markdown and JSON files
for md_file in markdown_files:
    with open(md_file, 'r') as f:
        markdown_text = f.read()
    html = markdown_to_html(markdown_text)
    
    for json_file in json_files:
        formatting = load_formatting_config(json_file)
        base_name = os.path.splitext(os.path.basename(md_file))[0]
        config_name = os.path.splitext(os.path.basename(json_file))[0]
        
        docx_path = os.path.join(docx_output_folder, f'{base_name}_{config_name}.docx')
        pdf_path = os.path.join(pdf_output_folder, f'{base_name}_{config_name}.pdf')
        
        html_to_docx(html, docx_path, formatting)
        docx_to_pdf(docx_path, pdf_path)