import unittest
from src.processing.markdown_to_html import markdown_to_html

class TestMarkdownToHtml(unittest.TestCase):
    def test_conversion(self):
        markdown_text = "# Title\n\nSome content."
        expected_html = "<h1>Title</h1>\n<p>Some content.</p>"
        self.assertEqual(markdown_to_html(markdown_text).strip(), expected_html)

if __name__ == "__main__":
    unittest.main()
