import unittest
from split_nodes_image import split_nodes_image
from textnode import TextNode, TextType


class TestSplitNodesImage(unittest.TestCase):
    def test_one_image(self):
        old_nodes = [
            TextNode(
                "Now i'll show you a cat image ![cat image](www.imgur.com/34dcksdf). cool right?",
                TextType.TEXT,
            ),
        ]

        result = split_nodes_image(old_nodes)

        self.assertEqual(
            result,
            [
                TextNode("Now i'll show you a cat image ", TextType.TEXT),
                TextNode("cat image", TextType.IMAGE, "www.imgur.com/34dcksdf"),
                TextNode(". cool right?", TextType.TEXT),
            ],
        )

    def test_one_image_at_start(self):
        old_nodes = [
            TextNode(
                "![cat image](www.imgur.com/34dcksdf). cool right?",
                TextType.TEXT,
            ),
        ]

        result = split_nodes_image(old_nodes)

        self.assertEqual(
            result,
            [
                TextNode("cat image", TextType.IMAGE, "www.imgur.com/34dcksdf"),
                TextNode(". cool right?", TextType.TEXT),
            ],
        )

    def test_one_image_at_end(self):
        old_nodes = [
            TextNode(
                "Now i'll show you a cat image ![cat image](www.imgur.com/34dcksdf)",
                TextType.TEXT,
            ),
        ]

        result = split_nodes_image(old_nodes)

        self.assertListEqual(
            result,
            [
                TextNode("Now i'll show you a cat image ", TextType.TEXT),
                TextNode("cat image", TextType.IMAGE, "www.imgur.com/34dcksdf"),
            ],
        )

    def test_multiple_images(self):
        old_nodes = [
            TextNode(
                "This is an image: ![to facebook](www.facebook.com) and here is another image: ![to youtube](https://www.google.ch) and some text",
                TextType.TEXT,
            ),
        ]

        result = split_nodes_image(old_nodes)

        self.assertListEqual(
            result,
            [
                TextNode("This is an image: ", TextType.TEXT),
                TextNode("to facebook", TextType.IMAGE, "www.facebook.com"),
                TextNode(" and here is another image: ", TextType.TEXT),
                TextNode("to youtube", TextType.IMAGE, "https://www.google.ch"),
                TextNode(" and some text", TextType.TEXT),
            ],
        )

    def test_multiple_images_without_gap(self):
        old_nodes = [
            TextNode(
                "This is an image: ![to facebook](www.facebook.com)![to youtube](https://www.google.ch) and some text",
                TextType.TEXT,
            ),
        ]

        result = split_nodes_image(old_nodes)

        self.assertListEqual(
            result,
            [
                TextNode("This is an image: ", TextType.TEXT),
                TextNode("to facebook", TextType.IMAGE, "www.facebook.com"),
                TextNode("to youtube", TextType.IMAGE, "https://www.google.ch"),
                TextNode(" and some text", TextType.TEXT),
            ],
        )
