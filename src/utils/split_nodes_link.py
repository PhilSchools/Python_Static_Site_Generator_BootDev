from classes.textnode import TextNode, TextType
from utils.extract_markdown_elements import extract_markdown_links


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:

    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        links = extract_markdown_links(text)

        for link in links:
            link_name, link_url = link
            sections = text.split(f"[{link_name}]({link_url})", 1)

            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.PLAIN_TEXT))

            link_node = TextNode(link_name, TextType.LINK_TEXT, link_url)
            new_nodes.append(link_node)
            text = sections[1]

        if text != "":
                new_nodes.append(TextNode(text, TextType.PLAIN_TEXT))

    return new_nodes
