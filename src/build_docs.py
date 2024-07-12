import os
import sys
from processing import markdown_to_html, html_to_docx, docx_to_pdf
from config import load_formatting_config
from utils.log_utils import init_logging, log_error

def create_output_folders(base_output_folder):
    docx_output_folder = os.path.join(base_output_folder, "docx")
    pdf_output_folder = os.path.join(base_output_folder, "pdf")
    os.makedirs(docx_output_folder, exist_ok=True)
    os.makedirs(pdf_output_folder, exist_ok=True)
    return docx_output_folder, pdf_output_folder

def main():
    try:
        log_file = init_logging()  # Initialize logging at the start of the script

        # Use hardcoded paths or environment variables for inputs
        markdown_folder = os.getenv("MARKDOWN_FOLDER", "samples/sample_resumes")
        json_folder = os.getenv("JSON_FOLDER", "samples/sample_jsons")
        output_folder = os.getenv("OUTPUT_FOLDER", "samples/output")

        # Collect all markdown and json files
        markdown_paths = [os.path.join(markdown_folder, f) for f in os.listdir(markdown_folder) if f.endswith('.md')]
        formatting_config_paths = [os.path.join(json_folder, f) for f in os.listdir(json_folder) if f.endswith('.json')]

        if markdown_paths and formatting_config_paths:
            docx_output_folder, pdf_output_folder = create_output_folders(output_folder)

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
            print("No markdown or json files found in the specified folders.")
    except Exception as e:
        log_error(e)
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
