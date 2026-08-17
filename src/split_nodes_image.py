
from extract_markdown_elements import *
from split_nodes_delimiter import *


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:

    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        images = extract_markdown_images(text)

        for image in images:
            image_alt, image_link = image
            sections = text.split(f"![{image_alt}]({image_link})", 1)

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.PLAIN_TEXT))

            image_node = TextNode(image_alt, TextType.IMAGE_TEXT, image_link)
            new_nodes.append(image_node)
            text = sections[1]

        if text != "":
                new_nodes.append(TextNode(text, TextType.PLAIN_TEXT))

    return new_nodes
