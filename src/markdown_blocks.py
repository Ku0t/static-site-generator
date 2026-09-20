import re
from enum import Enum
from htmlnode import HTMLNode, ParentNode
from inline_markdown import (
    split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes
)
from textnode import TextNode, TextType, text_node_to_html_node


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    ULIST = "unordered_list"
    OLIST = "ordered_list"

def markdown_to_blocks(markdown: str) -> list[str]:
    split_md = markdown.split("\n\n")
    strip_blocks = [b.strip() for b in split_md]
    clean_blocks = list(filter(lambda x: x != "", strip_blocks))
    return clean_blocks

def block_to_block_type(block:str) -> BlockType:
    headings = re.findall(r"#{1,6}", block)
    code = re.findall(r"```\n.*```", block, re.DOTALL)
    quote = re.findall(r">.*", block)
    unordered_list = re.findall(r"- .*", block)
    ordered_list = re.findall(r"\d+\..*", block)
    if len(headings) == 1:
        return BlockType.HEADING
    if len(code) > 0:
        return BlockType.CODE
    if len(quote) > 0:
        return BlockType.QUOTE
    if len(unordered_list) > 0:
        return BlockType.ULIST
    if len(ordered_list) > 0:
        return BlockType.OLIST
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        blocktype = block_to_block_type(block)
        if blocktype == BlockType.PARAGRAPH:
            block_node = ParentNode(f"p", text_to_children(block.replace("\n", " ")))
            html_nodes.append(block_node)
        if blocktype == BlockType.HEADING:
            hashes = block.count("#")
            block_node = ParentNode(f"h{hashes}", text_to_children(block.strip("# ")))
            html_nodes.append(block_node)
        if blocktype == BlockType.CODE:
            code_list = [code for code in block.strip("`").split("\n") if code.strip() != ""]
            code_text = "\n".join(code_list) + "\n"
            block_node = ParentNode("pre",[text_node_to_html_node(TextNode(code_text, TextType.CODE))])
            html_nodes.append(block_node)
        if blocktype == BlockType.QUOTE:
            quote_text = " ".join(block.replace("> ", "").split("\n"))
            block_node = ParentNode("blockquote",text_to_children(quote_text))
            html_nodes.append(block_node)
        if blocktype == BlockType.ULIST:
            unordered_list = block.split("\n")
            node_list = [ParentNode("li", text_to_children(node[2:])) for node in unordered_list]
            block_node = ParentNode("ul",node_list)
            html_nodes.append(block_node)
        if blocktype == BlockType.OLIST:
            ordered_list = block.split("\n")
            node_list = [ParentNode("li", text_to_children(node[node.index(".")+2:])) for node in ordered_list]
            block_node = ParentNode("ol",node_list)
            html_nodes.append(block_node)
    return ParentNode("div", html_nodes)

def text_to_children(text:str) -> list[HTMLNode]:
    text_nodes = text_to_textnodes(text)
    children = list(map(text_node_to_html_node, text_nodes))
    return children