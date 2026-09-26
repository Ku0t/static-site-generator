import unittest

from htmlnode import ParentNode, HTMLNode, LeafNode
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node, extract_title


class TestMarkdownToHTML(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks(self):
        heading = "###### Heading"
        blocktype = block_to_block_type(heading)
        self.assertEqual(
            blocktype,
            BlockType.HEADING,
        )
    
    def test_markdown_to_blocks(self):
        code = """
```
code
```
"""
        blocktype = block_to_block_type(heading)
        self.assertEqual(
            blocktype,
            BlockType.CODE,
        )
    
    def test_markdown_to_blocks(self):
        quote = """
>quote
> new line quote
"""
        blocktype = block_to_block_type(quote)
        self.assertEqual(
            blocktype,
            BlockType.QUOTE,
        )
    
    def test_markdown_to_blocks(self):
        unordered_list = """
- list item
- new line list
"""
        blocktype = block_to_block_type(unordered_list)
        self.assertEqual(
            blocktype,
            BlockType.ULIST,
        )
    
    def test_markdown_to_blocks(self):
        ordered_list = """
1. list item
2. new line list
"""
        blocktype = block_to_block_type(ordered_list)
        self.assertEqual(
            blocktype,
            BlockType.OLIST,
        )

    def test_markdown_to_blocks(self):
        paragraph = "paragraph"
        blocktype = block_to_block_type(paragraph)
        self.assertEqual(
            blocktype,
            BlockType.PARAGRAPH,
        )
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )


    def test_codeblock(self):
        md = """
    ```
This is text that _should_ remain
the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    
    def test_extract_title(self):
        md = "# Hello"
        title = extract_title(md)
        self.assertEqual(
            title,
            "Hello"
        )
if __name__ == "__main__":
    unittest.main()
