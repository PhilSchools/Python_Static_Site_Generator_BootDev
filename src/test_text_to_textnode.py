import unittest

from text_to_textnodes import text_to_textnodes, TextNode, TextType

class TestTextToTextNode(unittest.TestCase):
    def test_text_to_textnodes(self):
        test_nodes = []
        text = TextNode (
            "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)",
            TextType.PLAIN_TEXT
        )
        test_nodes.append(text)
        split_nodes = text_to_textnodes(test_nodes)
        self.assertEqual(len(split_nodes), 10)
        new_nodes = [
            TextNode("This is ", TextType.PLAIN_TEXT),
            TextNode("text", TextType.BOLD_TEXT),
            TextNode(" with an ", TextType.PLAIN_TEXT),
            TextNode("italic", TextType.ITALIC_TEXT),
            TextNode(" word and a ", TextType.PLAIN_TEXT),
            TextNode("code block", TextType.CODE_TEXT),
            TextNode(" and an ", TextType.PLAIN_TEXT),
            TextNode("obi wan image", TextType.IMAGE_TEXT, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.PLAIN_TEXT),
            TextNode("link", TextType.LINK_TEXT, "https://boot.dev"),
        ]
        self.assertListEqual(split_nodes, new_nodes)