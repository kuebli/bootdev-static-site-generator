from typing import List

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: List[TextNode], delimiter, text_type: TextType):
    new_nodes = []
    for node in old_nodes:
        index_start = node.text.find(delimiter) + len(delimiter)
        if index_start == -1:
            raise Exception()

        index_end = node.text.find(delimiter, index_start)
        if index_end == -1:
            raise Exception()

        text_transform = node.text[index_start:index_end]

        for part in node.text.split(delimiter):
            if part == text_transform:
                new_nodes.append(TextNode(part, text_type.value))
            elif len(part) > 0:
                new_nodes.append(TextNode(part, TextType.TEXT.value))
    return new_nodes
