from typing import List
from textnode import TextNode, TextType
from extract_markdown_links import extract_markdown_links


def split_nodes_link(old_nodes: List[TextNode]) -> List[TextNode]:
    nodes = []

    for node in old_nodes:
        links = extract_markdown_links(node.text)
        text = node.text

        for link in links:
            sections = text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections[0]) > 0:
                nodes.append(TextNode(sections[0], TextType.TEXT))
            nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            text = sections[1]

        if len(text) > 0:
            nodes.append(TextNode(text, TextType.TEXT))

    return nodes
