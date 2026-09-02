"""
src/utils/extract_title.py
Extracts the title/ h1 header ('# ...') from a given Markdown text.
"""

from classes.block_type import *
from utils.markdown_to_blocks import *


def extract_title(markdown: str) -> str | ValueError:
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.H1:
            return block.strip("#").strip()
    raise ValueError("No h1 title found in Markdown text.")