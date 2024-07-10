import os
import unittest
from src.processing.docx_to_pdf import docx_to_pdf

class TestDocxToPdf(unittest.TestCase):
    def test_conversion(self):
        docx_path = "output/test.docx"
        pdf_path = "output/test.pdf"
        docx_to_pdf(docx_path, pdf_path)
        # Check if the file is created
        self.assertTrue(os.path.exists(pdf_path))

if __name__ == "__main__":
    unittest.main()
