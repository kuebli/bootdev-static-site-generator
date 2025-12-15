from typing import List, Text
from textnode import TextNode, TextType
from extract_markdown_images import extract_markdown_images


def split_nodes_image(old_nodes: List[TextNode]) -> List[TextNode]:
    nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            nodes.append(node)
            continue

        images = extract_markdown_images(node.text)
        text = node.text

        for image in images:
            sections = text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections[0]) > 0:
                nodes.append(TextNode(sections[0], TextType.TEXT))
            nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            text = sections[1]

        if len(text) > 0:
            nodes.append(TextNode(text, TextType.TEXT))

    return nodes
