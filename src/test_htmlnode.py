import unittest

from htmlnode import HTMLNode


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