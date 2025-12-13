import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is anoter text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_not_in_texttype(self):
        node = TextNode("This is a text node", "text_italic")
        self.assertFalse(node.text_type in TextType._value2member_map_)

    def test_url_default_value(self):
        node = TextNode("This is a text node", "text_italic")
        self.assertIsNone(node.url)


if __name__ == "__main__":
    unittest.main()
