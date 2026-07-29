import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_1(self):
        html_node = HTMLNode("a", "This is a Link Value", None, {"href": "https://google.com", "target": "_blank"})
        stringified_should_be = ' href="https://google.com" target="_blank"'
        node_to_props = html_node.props_to_html()
        self.assertEqual(node_to_props, stringified_should_be)

    def test_props_to_html_2(self):
        html_node = HTMLNode("a", "This is a Link Value", None, {"href": "https://google.com", "target": "_blank"})
        stringified_should_not_be = 'href="https://google.com"target="_blank"'
        node_to_props = html_node.props_to_html()
        self.assertNotEqual(node_to_props, stringified_should_not_be)

    def test_props_to_html_3(self):
        html_node = HTMLNode("a", "This is a Link Value", None, {"href": "https://google.com", "target": "_blank"})
        stringified_should_not_be = '"href"="https://google.com"  "target"="_blank"'
        node_to_props = html_node.props_to_html()
        self.assertNotEqual(node_to_props, stringified_should_not_be)

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Google It", {"href": "https://google.com", "target": "_blank"})
        self.assertNotEqual(node.to_html(), "<a>Google It</a>")
        self.assertEqual(node.to_html(), '<a href="https://google.com" target="_blank">Google It</a>')

    def test_leaf_to_html_h1(self):
        node = LeafNode("h1", "Hello, world!")
        self.assertEqual(node.to_html(), "<h1>Hello, world!</h1>")
