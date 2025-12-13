from textnode import TextNode, TextType
from leafnode import LeafNode


def textnode_to_htmlnode(text_node: TextNode) -> LeafNode:
    if text_node.text_type not in TextType._value2member_map_:
        raise Exception("This text type is not supported")

    match text_node.text_type:
        case TextType.TEXT.value:
            return LeafNode("", text_node.text)
        case TextType.BOLD.value:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC.value:
            return LeafNode("i", text_node.text)
        case TextType.CODE.value:
            return LeafNode("code", text_node.text)
        case TextType.LINK.value:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE.value:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

    return LeafNode("", text_node.text)
