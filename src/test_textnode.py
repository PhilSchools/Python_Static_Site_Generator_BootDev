import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_not_equal(self):
        node = TextNode("This is not going to equal the next one", TextType.ITALIC_TEXT)
        node2 = TextNode("But I want to equal the one before me", TextType.ITALIC_TEXT)
        self.assertNotEqual(node, node2)

    def test_different_text_types(self):
        node = TextNode("The text will match", TextType.BOLD_TEXT)
        node2 = TextNode("The text will match", TextType.LINK_TEXT)
        self.assertNotEqual(node, node2)

    def test_url_mismatch(self):
        node = TextNode("The text will match", TextType.LINK_TEXT, None)
        node2 = TextNode("The text will match", TextType.LINK_TEXT, "https://not-match.com")
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold_text(self):
        html_node = text_node_to_html_node(TextNode("bold", TextType.BOLD_TEXT))
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "bold")

    def test_italic_text(self):
        html_node = text_node_to_html_node(TextNode("italic", TextType.ITALIC_TEXT))
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "italic")

    def test_code_text(self):
        html_node = text_node_to_html_node(TextNode("print('hello')", TextType.CODE_TEXT))
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "print('hello')")

    def test_link_text(self):
        html_node = text_node_to_html_node(
            TextNode("Boot.dev", TextType.LINK_TEXT, "https://boot.dev")
        )
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Boot.dev")
        self.assertEqual(html_node.props, {"href": "https://boot.dev"})

    def test_image_text(self):
        html_node = text_node_to_html_node(
            TextNode("A boot", TextType.IMAGE_TEXT, "https://example.com/boot.png")
        )
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "A boot")
        self.assertEqual(
            html_node.props,
            {"src": "https://example.com/boot.png", "alt": "A boot"},
        )

    def test_text_node_to_html_node_renders_html(self):
        html_node = text_node_to_html_node(TextNode("click me", TextType.LINK_TEXT, "/home"))
        self.assertEqual(html_node.to_html(), '<a href="/home">click me</a>')

    def test_unknown_text_type_raises_error(self):
        node = TextNode("unknown", "unknown")
        with self.assertRaises(ValueError):
            text_node_to_html_node(node)


if __name__ == "__main__":
    unittest.main()
