import unittest
from src.processing.markdown_to_formatted_docx import your_function_name


class TestMarkdownToFormattedDocx(unittest.TestCase):

    def test_your_function_name(self):
        # Arrange
        input_data = "your test input"
        expected_output = "your expected output"
        
        # Act
        result = your_function_name(input_data)
        
        # Assert
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()