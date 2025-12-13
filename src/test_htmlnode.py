import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_notimplementederror(self):
        node = HTMLNode("p", "Test")
        self.assertRaises(NotImplementedError, node.to_html)

    def test_props_to_html(self):
        props = {"href": "www.google.ch", "target": "_blank"}
        html = ' href="www.google.ch" target="_blank"'
        node = HTMLNode("p", "Test", props=props)

        self.assertEqual(node.props_to_html(), html)

    def test_defaults(self):
        node = HTMLNode()
        node_repr = node.__repr__()

        self.assertEqual(node_repr, "HTMLNode(None, None, None, None)")


if __name__ == "main":
    unittest.main()
