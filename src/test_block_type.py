import unittest

from block_type import BlockType, block_to_block_type


class TestBlockType(unittest.TestCase):
    def test_heading(self):
        for level in range(1, 7):
            with self.subTest(level=level):
                block = f"{'#' * level} Heading"
                self.assertEqual(block_to_block_type(block), BlockType.HEADING)

    def test_invalid_heading(self):
        invalid_headings = ["####### Too many hashes", "#Missing space"]
        for block in invalid_headings:
            with self.subTest(block=block):
                self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_code_block(self):
        block = "```\nprint('Hello, world!')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_incomplete_code_block(self):
        block = "```\nprint('Missing closing fence')"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_quote_block(self):
        block = "> First quoted line\n> Second quoted line"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)

    def test_mixed_quote_block(self):
        block = "> Quoted line\nThis line is not quoted"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_unordered_list(self):
        block = "- First item\n- Second item\n- Third item"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        block = "1. First item\n2. Second item\n3. Third item"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_out_of_sequence_ordered_list(self):
        block = "1. First item\n3. Third item"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_paragraph(self):
        block = "This is a regular paragraph.\nIt can span multiple lines."
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
