import os
import unittest
from src.processing.html_to_docx import html_to_docx

class TestHtmlToDocx(unittest.TestCase):
    def test_conversion(self):
        html_content = "<h1>Title</h1><p>Some content.</p>"
        docx_path = "output/test.docx"
        formatting = {}  # Provide appropriate formatting dict
        html_to_docx(html_content, docx_path, formatting)
        # Check if the file is created
        self.assertTrue(os.path.exists(docx_path))

if __name__ == "__main__":
    unittest.main()
