import os
import sys
import unittest
import src
from src.processing.markdown_to_html import markdown_to_html
from src.processing.html_to_docx import html_to_docx
from src.processing.docx_to_pdf import docx_to_pdf

class TestMarkdownToFormattedDocx(unittest.TestCase):

    def setUp(self):
        self.sample_resumes_dir = 'sample_resumes'
        self.sample_jsons_dir = 'sample_jsons'
        self.output_dir = 'output'
        self.docx_output_dir = os.path.join(self.output_dir, 'docx')
        self.pdf_output_dir = os.path.join(self.output_dir, 'pdf')

    def get_most_recent_file(self, directory, extension):
        files = [f for f in os.listdir(directory) if f.endswith(extension)]
        if not files:
            raise FileNotFoundError(f"No {extension} files found in {directory}")
        files.sort(key=lambda x: os.path.getmtime(os.path.join(directory, x)), reverse=True)
        return os.path.join(directory, files[0])

    def test_generate_resume(self):
        markdown_path = self.get_most_recent_file(self.sample_resumes_dir, '.md')
        json_path = self.get_most_recent_file(self.sample_jsons_dir, '.json')

        # Simulate command line arguments
        sys.argv = ['main.py', '--ci', json_path, markdown_path]

        # Test markdown to HTML
        with open(markdown_path, 'r', encoding='utf-8') as f:
            markdown_text = f.read()
        html_content = markdown_to_html(markdown_text)

        # Test HTML to DOCX
        docx_path = os.path.join(self.docx_output_dir, 'output.docx')
        html_to_docx(html_content, docx_path, json_path)

        # Test DOCX to PDF
        pdf_path = os.path.join(self.pdf_output_dir, 'output.pdf')
        docx_to_pdf(docx_path, pdf_path)

        # Verify the outputs
        self.assertTrue(os.path.exists(docx_path), f"Expected DOCX file {docx_path} does not exist.")
        self.assertTrue(os.path.exists(pdf_path), f"Expected PDF file {pdf_path} does not exist.")

if __name__ == '__main__':
    unittest.main()
