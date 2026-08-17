from split_nodes_link import *
from split_nodes_image import *
from split_nodes_delimiter import *


def split_nodes_code(text) -> list[TextNode]:
    return split_nodes_delimiter(text, "`", TextType.CODE_TEXT)


def split_nodes_bold(text) -> list[TextNode]:
    return split_nodes_delimiter(text, "**", TextType.BOLD_TEXT)


def split_nodes_italic(text) -> list[TextNode]:
    return split_nodes_delimiter(text, "_", TextType.ITALIC_TEXT)


def text_to_textnodes(text) -> list[TextNode]:
    return split_nodes_code(split_nodes_bold(split_nodes_italic(split_nodes_link(split_nodes_image(text)))))

