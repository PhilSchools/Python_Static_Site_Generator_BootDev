"""
src/utils/get_markdown_content_from_index.py

This module provides a function to extract Markdown content from content/index.md
or a specified file path.
"""

import os

MARKDOWN_INDEX = "content/index.md"
MARKDOWN_INDEX_PATH = os.path.join(os.getcwd(), MARKDOWN_INDEX)


def get_markdown_content(file=MARKDOWN_INDEX_PATH):
    with open(file, "r") as f:
        return f.read()