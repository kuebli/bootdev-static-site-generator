import unittest
from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_single_line(self):
        md = "# Test Title"
        result = extract_title(md)
        expected = "Test Title"
        self.assertEqual(result, expected)

    def test_multiple_lines(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

# here we have the title

- This is a list
- with items
"""
        result = extract_title(md)
        expected = "here we have the title"
        self.assertEqual(result, expected)

    def test_md_without_title(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line


- This is a list
- with items
"""
        self.assertRaises(Exception, lambda: extract_title, md)
