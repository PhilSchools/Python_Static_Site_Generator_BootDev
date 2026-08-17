import unittest

from split_nodes_image import *
from split_nodes_link import *


class TestSplitNodesImage(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png) and a little more text",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN_TEXT),
                TextNode("image", TextType.IMAGE_TEXT, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN_TEXT),
                TextNode("second image", TextType.IMAGE_TEXT, "https://i.imgur.com/3elNhQu.png"),
                TextNode(" and a little more text", TextType.PLAIN_TEXT),
            ],
            new_nodes,
        )

    def test_split_images_2(self):
        node = TextNode(
            "![image-1](https://i.imgur.com/zjjcJFK.png) it's an image, just one.",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image-1", TextType.IMAGE_TEXT, "https://i.imgur.com/zjjcJFK.png"),
                TextNode(" it's an image, just one.", TextType.PLAIN_TEXT),
            ],
            new_nodes,
        )

    def test_split_images_3(self):
        node = TextNode(
            "An Image -> ![image](https://i.imgur.com/zjjcJFK.png) and a Link -> [link](https://example.com) only the image should be caught",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("An Image -> ", TextType.PLAIN_TEXT),
                TextNode("image", TextType.IMAGE_TEXT, "https://i.imgur.com/zjjcJFK.png"),
                TextNode(" and a Link -> [link](https://example.com) only the image should be caught", TextType.PLAIN_TEXT),
            ],
            new_nodes,
        )
    def test_split_images_4(self):
        node = TextNode(
            "![image-1](https://i.imgur.com/zjjcJFK.png) ![image-2](https://i.imgur.com/3elNhQu.png) it's two images, just two.",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image-1", TextType.IMAGE_TEXT, "https://i.imgur.com/zjjcJFK.png"),
                TextNode(" ", TextType.PLAIN_TEXT),
                TextNode("image-2", TextType.IMAGE_TEXT, "https://i.imgur.com/3elNhQu.png"),
                TextNode(" it's two images, just two.", TextType.PLAIN_TEXT),
            ],
            new_nodes,
        )

    def test_split_images_5(self):
        node = TextNode(
            "[link](https://example.com) this is just one link",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("[link](https://example.com) this is just one link", TextType.PLAIN_TEXT),
            ],
            new_nodes,
        )


class TestSplitNodesLinks(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "[link](https://example.com)",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK_TEXT, "https://example.com"),
            ],
            new_nodes,
        )

    def test_split_links_2(self):
        node = TextNode(
            "[link](https://example.com) this is a link, just one link.",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("link", TextType.LINK_TEXT, "https://example.com"),
                TextNode(" this is a link, just one link.", TextType.PLAIN_TEXT),
            ],
            new_nodes,
        )

    def test_split_links_3(self):
        node = TextNode(
            "This is an Image NOT a Link and will not be captured ![image](https://example.com)",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is an Image NOT a Link and will not be captured ![image](https://example.com)", TextType.PLAIN_TEXT),
            ],
            new_nodes,
        )

    def test_split_links_4(self):
        node = TextNode(
            "This is TWO Links and will be captured as such [link-1](https://example.com) [link-2](https://example.com/two)",
            TextType.PLAIN_TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is TWO Links and will be captured as such ", TextType.PLAIN_TEXT),
                TextNode("link-1", TextType.LINK_TEXT, "https://example.com"),
                TextNode(" ", TextType.PLAIN_TEXT),
                TextNode("link-2", TextType.LINK_TEXT, "https://example.com/two"),
            ],
            new_nodes,
        )