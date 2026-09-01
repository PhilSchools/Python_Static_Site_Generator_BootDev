from classes.textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
        else:
            text = node.text
            splits = text.split(delimiter)

            # A matched pair of delimiters always yields an odd number of parts.
            if len(splits) % 2 == 0:
                raise ValueError(f"unmatched delimiter {delimiter!r} in {text!r}")

            for i, split in enumerate(splits):
                if split == "":
                    continue
                # Odd indices sit between a pair of delimiters; the rest stay plain.
                part_type = text_type if i % 2 == 1 else TextType.PLAIN_TEXT
                new_nodes.append(TextNode(split, part_type))

    return new_nodes
