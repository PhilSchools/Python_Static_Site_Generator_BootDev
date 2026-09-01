import unittest

from markdown_to_html_node import *


class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_single_paragraph(self):
        node = markdown_to_html_node("A plain paragraph")
        self.assertEqual(node.to_html(), "<div><p>A plain paragraph</p></div>")

    def test_multiline_paragraph(self):
        md = "First line\nsecond line\nthird line"
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><p>First line second line third line</p></div>",
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

    def test_h1_heading(self):
        node = markdown_to_html_node("# Main heading")
        self.assertEqual(node.to_html(), "<div><h1>Main heading</h1></div>")

    def test_h6_heading(self):
        node = markdown_to_html_node("###### Smallest heading")
        self.assertEqual(node.to_html(), "<div><h6>Smallest heading</h6></div>")

    def test_heading_with_inline_markdown(self):
        node = markdown_to_html_node("### A **bold** heading")
        self.assertEqual(
            node.to_html(),
            "<div><h3>A <b>bold</b> heading</h3></div>",
        )

    def test_single_line_codeblock(self):
        md = "```\nprint('hello')\n```"
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><pre><code>print('hello')\n</code></pre></div>",
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

    def test_multiple_codeblocks(self):
        md = "```\nfirst\n```\n\n```\nsecond\n```"
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><pre><code>first\n</code></pre><pre><code>second\n</code></pre></div>",
        )

    def test_single_line_quote(self):
        node = markdown_to_html_node("> A quoted sentence")
        self.assertEqual(
            node.to_html(),
            "<div><blockquote>A quoted sentence</blockquote></div>",
        )

    def test_multiline_quote(self):
        md = "> First line\n> Second line\n> Third line"
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><blockquote>First line Second line Third line</blockquote></div>",
        )

    def test_quote_with_inline_markdown(self):
        node = markdown_to_html_node("> This is **important** and _quoted_")
        self.assertEqual(
            node.to_html(),
            "<div><blockquote>This is <b>important</b> and <i>quoted</i></blockquote></div>",
        )

    def test_single_unordered_list_item(self):
        node = markdown_to_html_node("- One item")
        self.assertEqual(node.to_html(), "<div><ul><li>One item</li></ul></div>")

    def test_multiple_unordered_list_items(self):
        md = "- First item\n- Second item\n- Third item"
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><ul><li>First item</li><li>Second item</li><li>Third item</li></ul></div>",
        )

    def test_unordered_list_with_inline_markdown(self):
        md = "- A **bold** item\n- An _italic_ item"
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><ul><li>A <b>bold</b> item</li><li>An <i>italic</i> item</li></ul></div>",
        )

    def test_single_ordered_list_item(self):
        node = markdown_to_html_node("1. One item")
        self.assertEqual(node.to_html(), "<div><ol><li>One item</li></ol></div>")

    def test_multiple_ordered_list_items(self):
        md = "1. First item\n2. Second item\n3. Third item"
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><ol><li>First item</li><li>Second item</li><li>Third item</li></ol></div>",
        )

    def test_ordered_list_with_inline_markdown(self):
        md = "1. A `code` item\n2. A **bold** item"
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(),
            "<div><ol><li>A <code>code</code> item</li><li>A <b>bold</b> item</li></ol></div>",
        )
