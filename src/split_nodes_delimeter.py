from textnode import *


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
        else:
            splits = node.text.split(delimiter)

            for split in splits:
                if split == "":
                    continue
                new_nodes.append(TextNode(split, text_type))

    return new_nodes
