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
                subblocks = block.split("\n")
                subblocks_html_nodes = []
                for block in subblocks:
                    subblocks_html_nodes.append(
                        ParentNode("li", [LeafNode("", block[2:])])
                    )
                children.append(ParentNode("ul", subblocks_html_nodes))
            case BlockType.ORDERED_LIST:
                subblocks = block.split("\n")
                subblocks_html_nodes = []
                for block in subblocks:
                    subblocks_html_nodes.append(
                        ParentNode("li", [LeafNode("", block[2:])])
                    )
                children.append(ParentNode("ol", subblocks_html_nodes))

    parent_node = ParentNode("div", children)
    # print(f"parent_node: {parent_node}")
    # print(f"parent_node html: {parent_node.to_html()}")
    return parent_node
