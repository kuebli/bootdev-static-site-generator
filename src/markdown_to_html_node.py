from leafnode import LeafNode
from markdown_to_blocks import markdown_to_blocks
from block_to_block_type import block_to_block_type, BlockType
from text_to_textnodes import text_to_textnodes
from textnode_to_htmlnode import textnode_to_htmlnode
from parentnode import ParentNode


def markdown_to_html_node(document: str):
    children = []
    blocks = markdown_to_blocks(document)

    for block in blocks:
        children_block = []
        type = block_to_block_type(block)

        match type:
            case BlockType.PARAGRAPH:
                for text_node in text_to_textnodes(block.replace("\n", " ")):
                    children_block.append(textnode_to_htmlnode(text_node))
                children.append(ParentNode("p", children_block))
            case BlockType.HEADING:
                parts = block.split(" ", 1)
                for text_node in text_to_textnodes(parts[1]):
                    children_block.append(textnode_to_htmlnode(text_node))
                children.append(ParentNode(f"h{parts[0].count('#')}", children_block))
            case BlockType.CODE:
                code_node = LeafNode("code", block[3:-3])
                children.append(ParentNode("pre", [code_node]))
            case BlockType.QUOTE:
                for text_node in text_to_textnodes(block[2:]):
                    children_block.append(textnode_to_htmlnode(text_node))
                children.append(ParentNode("blockquote", children_block))
            case BlockType.UNORDERED_LIST:
                lis = []
                for li in map(lambda t: t[2:], block.split("\n")):
                    li_nodes = []
                    for text_node in text_to_textnodes(li):
                        li_nodes.append(textnode_to_htmlnode(text_node))
                    lis.append(ParentNode("li", li_nodes))
                children.append(ParentNode("ul", lis))
            case BlockType.ORDERED_LIST:
                lis = []
                for li in map(lambda t: t[3:], block.split("\n")):
                    li_nodes = []
                    for text_node in text_to_textnodes(li):
                        li_nodes.append(textnode_to_htmlnode(text_node))
                    lis.append(ParentNode("li", li_nodes))
                children.append(ParentNode("ol", lis))

    parent_node = ParentNode("div", children)
    return parent_node
