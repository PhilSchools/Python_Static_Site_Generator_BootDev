import unittest

from classes.textnode import TextNode, TextType, text_node_to_html_node
from utils.split_nodes_delimiter import split_nodes_delimiter


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

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter_1(self):
        node = TextNode("hello big world", TextType.PLAIN_TEXT)
        new_nodes = [node]
        split_nodes = split_nodes_delimiter(new_nodes, " ", TextType.PLAIN_TEXT)
        self.assertEqual(len(split_nodes), 3)
        self.assertEqual(split_nodes[0].text, "hello")
        self.assertEqual(split_nodes[1].text, "big")
        self.assertEqual(split_nodes[2].text, "world")

    def test_split_nodes_delimiter_2(self):
        node = TextNode("Hi there, your **chariot** awaits!", TextType.PLAIN_TEXT)
        new_nodes = [node]
        split_nodes = split_nodes_delimiter(new_nodes, "**", TextType.PLAIN_TEXT)
        self.assertEqual(len(split_nodes), 3)
        self.assertEqual(split_nodes[0].text, "Hi there, your ")
        self.assertEqual(split_nodes[0].text_type, TextType.PLAIN_TEXT)
        self.assertEqual(split_nodes[1].text, "chariot")
        self.assertEqual(split_nodes[1].text_type, TextType.PLAIN_TEXT)
        self.assertEqual(split_nodes[2].text, " awaits!")
        self.assertEqual(split_nodes[2].text_type, TextType.PLAIN_TEXT)

    def test_split_nodes_delimiter_3(self):
        node = TextNode("Hello **Bob**, I think that you will like this _delicious_ recipe!", TextType.PLAIN_TEXT)
        new_nodes = [node]
        split_nodes = split_nodes_delimiter(new_nodes, "**", TextType.PLAIN_TEXT)
        self.assertEqual(len(split_nodes), 3)
        self.assertEqual(split_nodes[0].text, "Hello ")
        self.assertEqual(split_nodes[0].text_type, TextType.PLAIN_TEXT)
        self.assertEqual(split_nodes[1].text, "Bob")
        self.assertEqual(split_nodes[1].text_type, TextType.PLAIN_TEXT)
        self.assertEqual(split_nodes[2].text, ", I think that you will like this _delicious_ recipe!")
        self.assertEqual(split_nodes[2].text_type, TextType.PLAIN_TEXT)
        split_nodes_2 = split_nodes_delimiter(new_nodes, "_", TextType.PLAIN_TEXT)
        self.assertEqual(len(split_nodes_2), 3)
        self.assertEqual(split_nodes_2[0].text, "Hello **Bob**, I think that you will like this ")
        self.assertEqual(split_nodes_2[0].text_type, TextType.PLAIN_TEXT)
        self.assertEqual(split_nodes_2[1].text, "delicious")
        self.assertEqual(split_nodes_2[1].text_type, TextType.PLAIN_TEXT)
        self.assertEqual(split_nodes_2[2].text, " recipe!")
        self.assertEqual(split_nodes_2[2].text_type, TextType.PLAIN_TEXT)

    def test_empty_list_returns_empty_list(self):
        self.assertEqual(split_nodes_delimiter([], "`", TextType.CODE_TEXT), [])

    def test_non_plain_nodes_pass_through_untouched(self):
        node = TextNode("already **bold**", TextType.BOLD_TEXT)
        split_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        self.assertEqual(split_nodes, [TextNode("already **bold**", TextType.BOLD_TEXT)])

    def test_non_plain_node_keeps_its_url(self):
        node = TextNode("Boot.dev", TextType.LINK_TEXT, "https://boot.dev")
        split_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        self.assertEqual(len(split_nodes), 1)
        self.assertEqual(split_nodes[0].url, "https://boot.dev")

    def test_text_without_delimiter_stays_plain(self):
        node = TextNode("no code here", TextType.PLAIN_TEXT)
        split_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        self.assertEqual(split_nodes, [TextNode("no code here", TextType.PLAIN_TEXT)])

    def test_only_delimited_text_gets_the_new_type(self):
        node = TextNode("This is `code` here", TextType.PLAIN_TEXT)
        split_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        self.assertEqual(
            split_nodes,
            [
                TextNode("This is ", TextType.PLAIN_TEXT),
                TextNode("code", TextType.CODE_TEXT),
                TextNode(" here", TextType.PLAIN_TEXT),
            ],
        )

    def test_delimiter_at_start_produces_no_leading_empty_node(self):
        node = TextNode("`code` at the start", TextType.PLAIN_TEXT)
        split_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        self.assertEqual(
            split_nodes,
            [
                TextNode("code", TextType.CODE_TEXT),
                TextNode(" at the start", TextType.PLAIN_TEXT),
            ],
        )

    def test_delimiter_at_end_produces_no_trailing_empty_node(self):
        node = TextNode("ends with `code`", TextType.PLAIN_TEXT)
        split_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        self.assertEqual(
            split_nodes,
            [
                TextNode("ends with ", TextType.PLAIN_TEXT),
                TextNode("code", TextType.CODE_TEXT),
            ],
        )

    def test_entire_text_is_delimited(self):
        node = TextNode("**everything**", TextType.PLAIN_TEXT)
        split_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        self.assertEqual(split_nodes, [TextNode("everything", TextType.BOLD_TEXT)])

    def test_multiple_delimited_sections_in_one_node(self):
        node = TextNode("`a` and `b` and `c`", TextType.PLAIN_TEXT)
        split_nodes = split_nodes_delimiter([node], "`", TextType.CODE_TEXT)
        self.assertEqual(
            split_nodes,
            [
                TextNode("a", TextType.CODE_TEXT),
                TextNode(" and ", TextType.PLAIN_TEXT),
                TextNode("b", TextType.CODE_TEXT),
                TextNode(" and ", TextType.PLAIN_TEXT),
                TextNode("c", TextType.CODE_TEXT),
            ],
        )

    def test_adjacent_delimited_sections(self):
        node = TextNode("**a****b**", TextType.PLAIN_TEXT)
        split_nodes = split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)
        self.assertEqual(
            split_nodes,
            [
                TextNode("a", TextType.BOLD_TEXT),
                TextNode("b", TextType.BOLD_TEXT),
            ],
        )

    def test_every_node_in_the_list_is_processed(self):
        nodes = [
            TextNode("first `one`", TextType.PLAIN_TEXT),
            TextNode("untouched", TextType.ITALIC_TEXT),
            TextNode("`two` second", TextType.PLAIN_TEXT),
        ]
        split_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE_TEXT)
        self.assertEqual(
            split_nodes,
            [
                TextNode("first ", TextType.PLAIN_TEXT),
                TextNode("one", TextType.CODE_TEXT),
                TextNode("untouched", TextType.ITALIC_TEXT),
                TextNode("two", TextType.CODE_TEXT),
                TextNode(" second", TextType.PLAIN_TEXT),
            ],
        )

    def test_unclosed_delimiter_raises_value_error(self):
        node = TextNode("unclosed **bold here", TextType.PLAIN_TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.BOLD_TEXT)


if __name__ == "__main__":
    unittest.main()
