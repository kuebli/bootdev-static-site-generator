import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType


class TestTextToTextnodes(unittest.TestCase):
    def test_inline(self):
        text = "this is regular, **this is bold** and `this is code`"
        result = text_to_textnodes(text)

        self.assertListEqual(
            result,
            [
                TextNode("this is regular, ", TextType.TEXT),
                TextNode("this is bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("this is code", TextType.CODE),
            ],
        )

    def test_intline_link(self):
        text = "this is regular, [to google](https://google.ch) **this is bold** and `this is code`"
        result = text_to_textnodes(text)

        self.assertListEqual(
            result,
            [
                TextNode("this is regular, ", TextType.TEXT),
                TextNode("to google", TextType.LINK, "https://google.ch"),
                TextNode(" ", TextType.TEXT),
                TextNode("this is bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("this is code", TextType.CODE),
            ],
        )

    def test_intline_image(self):
        text = "this is regular, ![cat image](https://google.ch/images/cat) **this is bold** and `this is code`"
        result = text_to_textnodes(text)

        self.assertListEqual(
            result,
            [
                TextNode("this is regular, ", TextType.TEXT),
                TextNode("cat image", TextType.IMAGE, "https://google.ch/images/cat"),
                TextNode(" ", TextType.TEXT),
                TextNode("this is bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("this is code", TextType.CODE),
            ],
        )

    def test_intline_image_and_link(self):
        text = "this is regular, ![cat image](https://google.ch/images/cat) **this is bold** and `this is code`[to facebook](www.facebook.com)"
        result = text_to_textnodes(text)

        self.assertListEqual(
            result,
            [
                TextNode("this is regular, ", TextType.TEXT),
                TextNode("cat image", TextType.IMAGE, "https://google.ch/images/cat"),
                TextNode(" ", TextType.TEXT),
                TextNode("this is bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("this is code", TextType.CODE),
                TextNode("to facebook", TextType.LINK, "www.facebook.com"),
            ],
        )


if __name__ == "__main__":
    unittest.main()
