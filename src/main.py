import os
import sys
from processing import markdown_to_html, html_to_docx, docx_to_pdf
from config import load_formatting_config
from utils import create_output_folders, select_files
from utils.log_utils import init_logging, log_error

def main():
    try:
        log_file = init_logging()  # Initialize logging at the start of the script

        if len(sys.argv) > 1 and sys.argv[1] == '--ci':
            # Running in a CI environment
            formatting_config_paths = sys.argv[2].split(',')
            markdown_paths = sys.argv[3].split(',')
        else:
            # Running interactively
            formatting_config_paths = select_files("Select the JSON formatting configuration files", [("JSON files", "*.json")])
            markdown_paths = select_files("Select the Markdown files", [("Markdown files", "*.md")])

        if markdown_paths and formatting_config_paths:
            docx_output_folder, pdf_output_folder = create_output_folders()
            for markdown_path in markdown_paths:
                with open(markdown_path, 'r', encoding='utf-8') as f:
                    markdown_text = f.read()
                html_content = markdown_to_html(markdown_text)
                for formatting_config_path in formatting_config_paths:
                    formatting = load_formatting_config(formatting_config_path)
                    base_filename = os.path.splitext(os.path.basename(markdown_path))[0]
                    formatting_name = os.path.splitext(os.path.basename(formatting_config_path))[0]
                    docx_filename = f"{base_filename}_{formatting_name}.docx"
                    docx_path = os.path.join(docx_output_folder, docx_filename)
                    html_to_docx(html_content, docx_path, formatting)
                    print(f"DOCX file saved to {docx_path}")
                    pdf_filename = f"{base_filename}_{formatting_name}.pdf"
                    pdf_path = os.path.join(pdf_output_folder, pdf_filename)
                    docx_to_pdf(docx_path, pdf_path)
                    print(f"PDF file saved to {pdf_path}")
        else:
            print("File selection cancelled.")
    except Exception as e:
        log_error(e)

if __name__ == "__main__":
    main()
