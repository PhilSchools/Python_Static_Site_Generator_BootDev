import unittest

from classes.htmlnode import HTMLNode, LeafNode, ParentNode


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


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child1 = LeafNode("b", "Bold text")
        child2 = LeafNode(None, " Normal text ")
        child3 = LeafNode("i", "italic text")

        parent = ParentNode("p", [child1, child2, child3])
        self.assertEqual(
            parent.to_html(),
            "<p><b>Bold text</b> Normal text <i>italic text</i></p>"
        )

    def test_to_html_with_props(self):
        child = LeafNode("span", "hello")
        parent = ParentNode("div", [child], {"id": "main", "class": "container"})

        # Note: dict ordering in modern Python is insertion order
        self.assertEqual(
            parent.to_html(),
            '<div id="main" class="container"><span>hello</span></div>'
        )

    def test_to_html_parent_and_child_both_have_props(self):
        child = LeafNode("a", "click me", {"href": "https://google.com"})
        parent = ParentNode("div", [child], {"class": "wrapper"})

        self.assertEqual(
            parent.to_html(),
            '<div class="wrapper"><a href="https://google.com">click me</a></div>'
        )

    def test_to_html_deeply_nested(self):
        node = ParentNode("div", [
            ParentNode("ul", [
                ParentNode("li", [
                    LeafNode("b", "deep item")
                ])
            ])
        ])
        self.assertEqual(
            node.to_html(),
            "<div><ul><li><b>deep item</b></li></ul></div>"
        )

    def test_to_html_missing_tag_raises_error(self):
        child = LeafNode("span", "text")
        parent = ParentNode(None, [child])

        with self.assertRaises(ValueError):
            parent.to_html()

    def test_to_html_missing_children_raises_error(self):
        parent1 = ParentNode("div", [])
        parent2 = ParentNode("div", None)

        with self.assertRaises(ValueError):
            parent1.to_html()

        with self.assertRaises(ValueError):
            parent2.to_html()

    def test_to_html_mixed_leaf_and_parent_siblings(self):
        inline_text = LeafNode(None, "Welcome: ")
        bold_name = LeafNode("b", "Alice")
        nested_badge = ParentNode("span", [LeafNode("i", "Admin")], {"class": "badge"})

        parent = ParentNode("div", [inline_text, bold_name, nested_badge])
        self.assertEqual(
            parent.to_html(),
            '<div>Welcome: <b>Alice</b><span class="badge"><i>Admin</i></span></div>'
        )
