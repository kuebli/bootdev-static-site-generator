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
            TextNode("this is regular, ", TextType.TEXT),
            TextNode("this is bold", TextType.BOLD),
            TextNode(" but this is regular again.", TextType.TEXT),
        ]

        self.assertEqual(new_nodes, expected)

    def test_italic(self):
        old_nodes = [
            TextNode("_This is italic_ and this is regular", TextType.TEXT),
        ]

        new_nodes = split_nodes_delimiter(old_nodes, "_", TextType.ITALIC)

        expected = [
            TextNode("This is italic", TextType.ITALIC),
            TextNode(" and this is regular", TextType.TEXT),
        ]

        self.assertEqual(new_nodes, expected)

    def test_code(self):
        old_nodes = [
            TextNode("This part is not code, `but this one is`", TextType.TEXT),
        ]

        new_nodes = split_nodes_delimiter(old_nodes, "`", TextType.CODE)

        expected = [
            TextNode("This part is not code, ", TextType.TEXT),
            TextNode("but this one is", TextType.CODE),
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
            TextNode("this is regular, ", TextType.TEXT),
            TextNode("this is bold", TextType.BOLD),
            TextNode(" but this is regular again.", TextType.TEXT),
            TextNode("this is regular, ", TextType.TEXT),
            TextNode("this is bold", TextType.BOLD),
        ]

        self.assertEqual(new_nodes, expected)
