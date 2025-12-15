import unittest
from textnode_to_htmlnode import textnode_to_htmlnode
from textnode import TextNode, TextType


class TextTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        text_node = TextNode("text_node", TextType.TEXT)
        html_node = textnode_to_htmlnode(text_node)
        self.assertEqual(html_node.to_html(), "text_node")

    def test_bold(self):
        bold_node = TextNode("bold_node", TextType.BOLD)
        html_node = textnode_to_htmlnode(bold_node)
        self.assertEqual(html_node.to_html(), "<b>bold_node</b>")

    def test_italic(self):
        italic_node = TextNode("italic_node", TextType.ITALIC)
        html_node = textnode_to_htmlnode(italic_node)
        self.assertEqual(html_node.to_html(), "<i>italic_node</i>")

    def test_code(self):
        code_node = TextNode("code_node", TextType.CODE)
        html_node = textnode_to_htmlnode(code_node)
        self.assertEqual(html_node.to_html(), "<code>code_node</code>")

    def test_a(self):
        anker_node = TextNode("anker_node", TextType.LINK, "www.google.ch")
        html_node = textnode_to_htmlnode(anker_node)
        self.assertEqual(html_node.to_html(), '<a href="www.google.ch">anker_node</a>')

    def test_img(self):
        img_node = TextNode("img_alt", TextType.IMAGE, "www.google.ch")
        html_node = textnode_to_htmlnode(img_node)
        self.assertEqual(
            html_node.to_html(), '<img src="www.google.ch" alt="img_alt"></img>'
        )
