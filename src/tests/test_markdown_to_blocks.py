import unittest

from utils.markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
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

    def test_single_block(self):
        blocks = markdown_to_blocks("This is one paragraph.")
        self.assertEqual(blocks, ["This is one paragraph."])

    def test_multiple_paragraphs(self):
        md = "First paragraph.\n\nSecond paragraph.\n\nThird paragraph."
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            ["First paragraph.", "Second paragraph.", "Third paragraph."],
        )

    def test_strips_surrounding_whitespace_from_each_block(self):
        md = "  First paragraph.  \n\n\tSecond paragraph.\t"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["First paragraph.", "Second paragraph."])

    def test_preserves_single_newlines_inside_block(self):
        md = "First line\nSecond line\nThird line"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["First line\nSecond line\nThird line"])

    def test_preserves_indentation_inside_block(self):
        md = "- Parent item\n  - Nested item\n  - Another nested item"
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            ["- Parent item\n  - Nested item\n  - Another nested item"],
        )

    def test_preserves_markdown_syntax(self):
        md = "# Heading\n\n> A **bold** quote with a [link](https://example.com)"
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            ["# Heading", "> A **bold** quote with a [link](https://example.com)"],
        )

    def test_ignores_extra_blank_lines_between_blocks(self):
        md = "First block.\n\n\n\nSecond block."
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["First block.", "Second block."])

    def test_empty_markdown(self):
        blocks = markdown_to_blocks("")
        self.assertEqual(blocks, [])

    def test_whitespace_only_markdown(self):
        blocks = markdown_to_blocks("  \n\n\t\n\n  ")
        self.assertEqual(blocks, [])
