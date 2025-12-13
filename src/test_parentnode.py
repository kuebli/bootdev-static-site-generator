import unittest
from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html_ul(self):
        children = [
            LeafNode("li", "Test li 1"),
            LeafNode("li", "Test li 2"),
            LeafNode("li", "Test li 3"),
            LeafNode("li", "Test li 4"),
        ]
        node = ParentNode("ul", children, {"class": "text-red-200"})
        html = ""
        for i in range(0, 4):
            html += f"<li>Test li {i + 1}</li>"
        self.assertEqual(node.to_html(), f'<ul class="text-red-200">{html}</ul>')

    def test_to_html_div_with_grandchildren(self):
        grandchildren = [
            LeafNode("li", "Test li 1"),
            LeafNode("li", "Test li 2"),
            LeafNode("li", "Test li 3"),
            LeafNode("li", "Test li 4"),
        ]
        children = [
            ParentNode("ul", grandchildren),
            LeafNode("p", "Text p"),
        ]
        node = ParentNode("div", children)

        html = ""
        for i in range(0, 4):
            html += f"<li>Test li {i + 1}</li>"

        self.assertEqual(node.to_html(), f"<div><ul>{html}</ul><p>Text p</p></div>")

    def test_to_thml_no_tag_exception(self):
        children = [
            LeafNode("li", "Test li 1"),
            LeafNode("li", "Test li 2"),
            LeafNode("li", "Test li 3"),
            LeafNode("li", "Test li 4"),
        ]

        node = ParentNode("", children, {"class": "text-red-200"})
        html = ""
        for i in range(0, 4):
            html += f"<li>Test li {i + 1}</li>"

        self.assertRaises(ValueError, node.to_html)

    def test_to_thml_no_children_exception(self):
        node = ParentNode("div", [])
        self.assertRaises(ValueError, node.to_html)
