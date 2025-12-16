import unittest
from markdown_to_html_node import markdown_to_html_node


class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_one_line_paragraph(self):
        text = "this is regular **and this is bold**"
        expected = "<div><p>this is regular <b>and this is bold</b></p></div>"

        result = markdown_to_html_node(text)
        self.assertEqual(result.to_html(), expected)

    def test_one_line_heading_6(self):
        text = "###### Heading 6 i hope **and this is bold**"
        expected = "<div><h6>Heading 6 i hope <b>and this is bold</b></h6></div>"

        result = markdown_to_html_node(text)
        print(f"RESULT: {result.to_html()}")
        self.assertEqual(result.to_html(), expected)

    def test_one_line_code(self):
        text = "```This is regular and _this is italic_```"
        expected = (
            "<div><pre><code>This is regular and _this is italic_</code></pre></div>"
        )

        result = markdown_to_html_node(text)
        self.assertEqual(result.to_html(), expected)

    def test_one_line_blockquote(self):
        text = "> this is a quote"
        expected = "<div><blockquote>this is a quote</blockquote></div>"

        result = markdown_to_html_node(text)
        self.assertEqual(result.to_html(), expected)

    def test_one_line_unordered_list(self):
        text = """
- ul item 1
- ul item 2
- ul item 3
"""
        expected = (
            "<div><ul><li>ul item 1</li><li>ul item 2</li><li>ul item 3</li></ul></div>"
        )

        result = markdown_to_html_node(text)
        self.assertEqual(result.to_html(), expected)

    def test_one_line_ordered_list(self):
        text = """
1. ol item 1
2. ol item 2
3. ol item 3
"""
        expected = (
            "<div><ol><li>ol item 1</li><li>ol item 2</li><li>ol item 3</li></ol></div>"
        )

        result = markdown_to_html_node(text)

        self.assertEqual(result.to_html(), expected)

    def test_multiple_lines(self):
        text = """
### Heading 3

1. ol item 1
2. ol item 2
3. ol item 3
"""
        expected = "<div><h3>Heading 3</h3><ol><li>ol item 1</li><li>ol item 2</li><li>ol item 3</li></ol></div>"

        result = markdown_to_html_node(text)
        self.assertEqual(result.to_html(), expected)

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
