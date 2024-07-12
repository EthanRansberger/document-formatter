import unittest
import os
import sys

# Add the src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from main import main

class TestBuildDocs(unittest.TestCase):
    def setUp(self):
        self.sample_resumes_dir = "samples/sample_resumes"
        self.sample_jsons_dir = "samples/sample_jsons"
        self.output_dir = "samples/output"
        self.cleanup_output_dir()

    def cleanup_output_dir(self):
        if os.path.exists(self.output_dir):
            for file in os.listdir(self.output_dir):
                file_path = os.path.join(self.output_dir, file)
                if os.path.isfile(file_path):
                    os.unlink(file_path)

    def test_generate_all_combinations(self):
        # Run the main script to generate documents
        main()

        # Verify if the output files are generated
        self.assertTrue(os.path.exists(self.output_dir))
        output_files = os.listdir(self.output_dir)
        self.assertGreater(len(output_files), 0, "No files generated in the output directory.")

        expected_docx_files = set()
        expected_pdf_files = set()
        
        markdown_files = [os.path.join(self.sample_resumes_dir, f) for f in os.listdir(self.sample_resumes_dir) if f.endswith('.md')]
        json_files = [os.path.join(self.sample_jsons_dir, f) for f in os.listdir(self.sample_jsons_dir) if f.endswith('.json')]

        for md_file in markdown_files:
            for json_file in json_files:
                base_name_md = os.path.splitext(os.path.basename(md_file))[0]
                base_name_json = os.path.splitext(os.path.basename(json_file))[0]
                expected_docx_files.add(f"{base_name_md}_{base_name_json}.docx")
                expected_pdf_files.add(f"{base_name_md}_{base_name_json}.pdf")
        
        generated_files = set(output_files)
        self.assertTrue(expected_docx_files.issubset(generated_files), f"Missing DOCX files: {expected_docx_files - generated_files}")
        self.assertTrue(expected_pdf_files.issubset(generated_files), f"Missing PDF files: {expected_pdf_files - generated_files}")

    def tearDown(self):
        self.cleanup_output_dir()

if __name__ == "__main__":
    unittest.main()
