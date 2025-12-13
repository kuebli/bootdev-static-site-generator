import unittest
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_bold(self):
        old_nodes = [
            TextNode(
                "this is regular, **this is bold** but this is regular again.",
                TextType.TEXT,
            ),
        ]

        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)

        expected = [
            TextNode("this is regular, ", "text"),
            TextNode("this is bold", "bold"),
            TextNode(" but this is regular again.", "text"),
        ]

        self.assertEqual(new_nodes, expected)

    def test_italic(self):
        old_nodes = [
            TextNode("_This is italic_ and this is regular", TextType.TEXT),
        ]

        new_nodes = split_nodes_delimiter(old_nodes, "_", TextType.ITALIC)

        expected = [
            TextNode("This is italic", "italic"),
            TextNode(" and this is regular", "text"),
        ]

        self.assertEqual(new_nodes, expected)

    def test_code(self):
        old_nodes = [
            TextNode("This part is not code, `but this one is`", TextType.TEXT),
        ]

        new_nodes = split_nodes_delimiter(old_nodes, "`", TextType.CODE)

        expected = [
            TextNode("This part is not code, ", "text"),
            TextNode("but this one is", "code"),
        ]

        self.assertEqual(new_nodes, expected)

    def test_bold_multiple_old_nodes(self):
        old_nodes = [
            TextNode(
                "this is regular, **this is bold** but this is regular again.",
                TextType.TEXT,
            ),
            TextNode(
                "this is regular, **this is bold**",
                TextType.TEXT,
            ),
        ]

        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)

        expected = [
            TextNode("this is regular, ", "text"),
            TextNode("this is bold", "bold"),
            TextNode(" but this is regular again.", "text"),
            TextNode("this is regular, ", "text"),
            TextNode("this is bold", "bold"),
        ]

        self.assertEqual(new_nodes, expected)
