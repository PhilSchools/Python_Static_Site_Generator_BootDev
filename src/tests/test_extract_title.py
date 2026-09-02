import unittest

from utils.extract_title import *


class TestExtractTitle(unittest.TestCase):
    def test_extract_title_1(self):
        md = """
# This Is a Great Article

It really is not about anything at all.
This is **JUST** a test, and the Markdown syntax might not even be right.

### But

Nobody Cares, I just need to know if the h1 Title is properly extracted by:
```
src/utils/extract_title.py
```

So, there you have it.
"""
        self.assertEqual(extract_title(md), "This Is a Great Article")

    def test_extract_title_from_title_only_document(self):
        self.assertEqual(extract_title("# Standalone Title"), "Standalone Title")

    def test_extract_title_after_paragraph(self):
        md = "An introductory paragraph.\n\n# Article Title"
        self.assertEqual(extract_title(md), "Article Title")

    def test_extract_title_after_lower_level_headings(self):
        md = "## Section\n\n#### Subsection\n\n# Article Title"
        self.assertEqual(extract_title(md), "Article Title")

    def test_extract_title_returns_first_h1(self):
        md = "# First Title\n\nSome content.\n\n# Second Title"
        self.assertEqual(extract_title(md), "First Title")

    def test_extract_title_preserves_inline_markdown(self):
        md = "# A **Bold** and _Italic_ Title"
        self.assertEqual(extract_title(md), "A **Bold** and _Italic_ Title")

    def test_extract_title_preserves_hash_inside_title(self):
        md = "# Using C# in a Title"
        self.assertEqual(extract_title(md), "Using C# in a Title")

    def test_extract_title_ignores_heading_without_space(self):
        md = "#Not a Heading\n\n# Valid Title"
        self.assertEqual(extract_title(md), "Valid Title")

    def test_extract_title_ignores_h1_inside_code_block(self):
        md = "```\n# Not a Title\n```\n\n# Valid Title"
        self.assertEqual(extract_title(md), "Valid Title")

    def test_extract_title_raises_value_error_for_h2_through_h6(self):
        md = "\n\n".join(f"{'#' * level} Heading" for level in range(2, 7))
        with self.assertRaisesRegex(ValueError, "No h1 title found"):
            extract_title(md)

    def test_extract_title_raises_value_error_for_empty_markdown(self):
        with self.assertRaisesRegex(ValueError, "No h1 title found"):
            extract_title("")
