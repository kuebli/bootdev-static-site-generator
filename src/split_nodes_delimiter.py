from typing import List

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: List[TextNode], delimiter, text_type: TextType):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.LINK or node.text_type == TextType.IMAGE:
            new_nodes.append(node)
            continue

        index_start = node.text.find(delimiter)

        if index_start == -1:
            new_nodes.append(node)
            continue

        index_start += len(delimiter)

        index_end = node.text.find(delimiter, index_start)

        if index_end == -1:
            raise Exception(index_start, index_end, old_nodes)

        text_transform = node.text[index_start:index_end]

        for part in node.text.split(delimiter):
            if part == text_transform:
                new_nodes.append(TextNode(part, text_type))
            elif len(part) > 0:
                new_nodes.append(TextNode(part, TextType.TEXT))
    return new_nodes
