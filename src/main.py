import os
import sys
import tkinter as tk
from tkinter import filedialog
from processing import markdown_to_html, html_to_docx, docx_to_pdf
from config import load_formatting_config
from utils.log_utils import init_logging, log_error

def create_output_folders(docx_output_folder, pdf_output_folder):
    os.makedirs(docx_output_folder, exist_ok=True)
    os.makedirs(pdf_output_folder, exist_ok=True)

def select_files(file_types, title):
    root = tk.Tk()
    root.withdraw()
    files = filedialog.askopenfilenames(title=title, filetypes=file_types)
    return root.tk.splitlist(files)

def select_folder(title):
    root = tk.Tk()
    root.withdraw()
    folder = filedialog.askdirectory(title=title)
    return folder

def main():
    try:
        log_file = init_logging()  # Initialize logging at the start of the script

        # Select Markdown files
        markdown_paths = select_files([("Markdown files", "*.md")], "Select Markdown Files")
        
        # Select JSON files
        formatting_config_paths = select_files([("JSON files", "*.json")], "Select JSON Formatting Files")

        if markdown_paths and formatting_config_paths:
            # Select output folders
            docx_output_folder = select_folder("Select DOCX Output Folder")
            pdf_output_folder = select_folder("Select PDF Output Folder")
            create_output_folders(docx_output_folder, pdf_output_folder)

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
            print("No markdown or json files selected.")
    except Exception as e:
        log_error(e)
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
