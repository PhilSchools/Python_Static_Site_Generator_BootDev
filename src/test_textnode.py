import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()
