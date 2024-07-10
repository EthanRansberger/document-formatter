import os
import sys
import unittest
from src.markdown_to_formatted_docx import main as generate_resume

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

        sys.argv = ['markdown_to_formatted_docx.py', '--ci', json_path, markdown_path]
        generate_resume()

        # Check if output files are generated
        base_filename = os.path.splitext(os.path.basename(markdown_path))[0]
        formatting_name = os.path.splitext(os.path.basename(json_path))[0]
        expected_docx = os.path.join(self.docx_output_dir, f"{base_filename}_{formatting_name}.docx")
        expected_pdf = os.path.join(self.pdf_output_dir, f"{base_filename}_{formatting_name}.pdf")

        self.assertTrue(os.path.exists(expected_docx), f"Expected DOCX file {expected_docx} does not exist.")
        self.assertTrue(os.path.exists(expected_pdf), f"Expected PDF file {expected_pdf} does not exist.")

if __name__ == '__main__':
    unittest.main()
