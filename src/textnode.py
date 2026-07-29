from enum import Enum

from htmlnode import *


class TextType(Enum):
    PLAIN_TEXT = "plain"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK_TEXT = "link"
    IMAGE_TEXT = "image"

class TextNode:

    def __init__(self, text, text_type, url=None):

        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: object) -> bool:

        if not isinstance(other, TextNode):
            return NotImplemented

        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):

        return f"{type(self).__name__}({self.text!r}, {self.text_type.value!r}, {self.url!r})"


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    node = text_node
    text = text_node.text
    url = text_node.url
    txt_type = node.text_type

    match txt_type:
        case TextType.PLAIN_TEXT:
            return LeafNode(None, text)
        case TextType.BOLD_TEXT:
            return LeafNode("b", text)
        case TextType.ITALIC_TEXT:
            return LeafNode("i", text)
        case TextType.CODE_TEXT:
            return LeafNode("code", text)
        case TextType.LINK_TEXT:
            return LeafNode("a", text, {"href": url})
        case TextType.IMAGE_TEXT:
            return LeafNode("img", text, {"src": url, "alt": text})

        case _:
            raise ValueError("Unknown TextType")






