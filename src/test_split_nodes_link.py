import unittest
from split_nodes_link import split_nodes_link
from textnode import TextNode, TextType


class TestSplitNodesImage(unittest.TestCase):
    def test_one_link(self):
        old_nodes = [
            TextNode(
                "Now i'll show you a cat link [cat link](www.imgur.com/34dcksdf). cool right?",
                TextType.TEXT,
            ),
        ]

        result = split_nodes_link(old_nodes)

        self.assertEqual(
            result,
            [
                TextNode("Now i'll show you a cat link ", TextType.TEXT),
                TextNode("cat link", TextType.LINK, "www.imgur.com/34dcksdf"),
                TextNode(". cool right?", TextType.TEXT),
            ],
        )

    def test_one_link_at_start(self):
        old_nodes = [
            TextNode(
                "[cat link](www.imgur.com/34dcksdf). cool right?",
                TextType.TEXT,
            ),
        ]

        result = split_nodes_link(old_nodes)

        self.assertEqual(
            result,
            [
                TextNode("cat link", TextType.LINK, "www.imgur.com/34dcksdf"),
                TextNode(". cool right?", TextType.TEXT),
            ],
        )

    def test_one_link_at_end(self):
        old_nodes = [
            TextNode(
                "Now i'll show you a cat link [cat link](www.imgur.com/34dcksdf)",
                TextType.TEXT,
            ),
        ]

        result = split_nodes_link(old_nodes)

        self.assertListEqual(
            result,
            [
                TextNode("Now i'll show you a cat link ", TextType.TEXT),
                TextNode("cat link", TextType.LINK, "www.imgur.com/34dcksdf"),
            ],
        )

    def test_multiple_links(self):
        old_nodes = [
            TextNode(
                "This is an link: [to facebook](www.facebook.com) and here is another link: [to youtube](https://www.google.ch) and some text",
                TextType.TEXT,
            ),
        ]

        result = split_nodes_link(old_nodes)

        self.assertListEqual(
            result,
            [
                TextNode("This is an link: ", TextType.TEXT),
                TextNode("to facebook", TextType.LINK, "www.facebook.com"),
                TextNode(" and here is another link: ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.google.ch"),
                TextNode(" and some text", TextType.TEXT),
            ],
        )

    def test_multiple_links_without_gap(self):
        old_nodes = [
            TextNode(
                "This is an link: [to facebook](www.facebook.com)[to youtube](https://www.google.ch) and some text",
                TextType.TEXT,
            ),
        ]

        result = split_nodes_link(old_nodes)

        self.assertListEqual(
            result,
            [
                TextNode("This is an link: ", TextType.TEXT),
                TextNode("to facebook", TextType.LINK, "www.facebook.com"),
                TextNode("to youtube", TextType.LINK, "https://www.google.ch"),
                TextNode(" and some text", TextType.TEXT),
            ],
        )
