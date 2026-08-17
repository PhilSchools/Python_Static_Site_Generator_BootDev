import unittest

from extract_markdown_elements import *


class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images_1(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_2(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/pn77fh23.png) and another ![image-3](https://i.imgur.com/87ee54jt.png)"
        )
        self.assertListEqual(
            [("image", "https://i.imgur.com/pn77fh23.png"), ("image-3", "https://i.imgur.com/87ee54jt.png")],
            matches
        )

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_markdown_links_1(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://example.com)"
        )
        self.assertListEqual([("link", "https://example.com")], matches)

    def test_extract_markdown_links_2(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://example.com) and another [link-2](https://example.com)"
        )
        self.assertListEqual(
            [("link", "https://example.com"), ("link-2", "https://example.com")],
            matches
        )


