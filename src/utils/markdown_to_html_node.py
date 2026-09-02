from classes.block_type import BlockType, block_to_block_type
from classes.htmlnode import HTMLNode, ParentNode
from classes.textnode import TextNode, TextType, text_node_to_html_node
from utils.markdown_to_blocks import markdown_to_blocks
from utils.text_to_textnodes import text_to_textnodes


def markdown_to_html_node(md: str):
    blocks = markdown_to_blocks(md)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)

        match block_type:
            case BlockType.CODE:
                block_clean = clean_code_block(block)
                text_node = TextNode(block_clean, TextType.CODE_TEXT)
                text_html = text_node_to_html_node(text_node)
                parent = ParentNode("pre", [text_html])
                children.append(parent)

            case BlockType.PARAGRAPH:
                paragraph = " ".join(line.strip() for line in block.split("\n"))
                parent = ParentNode("p", text_to_children(paragraph))
                children.append(parent)

            case BlockType.H1 | BlockType.HEADING:
                heading = block.lstrip("#").strip()
                parent = ParentNode(heading_type(block), text_to_children(heading))
                children.append(parent)

            case BlockType.QUOTE:
                quote = " ".join(line.lstrip(">").strip() for line in block.split("\n"))
                parent = ParentNode("blockquote", text_to_children(quote))
                children.append(parent)

            case BlockType.UNORDERED_LIST:
                list_items = []
                for line in block.split("\n"):
                    list_items.append(ParentNode("li", text_to_children(line[2:])))
                children.append(ParentNode("ul", list_items))

            case BlockType.ORDERED_LIST:
                list_items = []
                for line in block.split("\n"):
                    item = line.split(". ", 1)[1]
                    list_items.append(ParentNode("li", text_to_children(item)))
                children.append(ParentNode("ol", list_items))

            case _:
                raise ValueError("Invalid block type")
    return ParentNode("div", children)


def heading_type(block: str) -> str:
    num_hash = len(block) - len(block.lstrip("#"))
    if 0 < num_hash <= 6:
        return f"h{num_hash}"
    raise ValueError("Invalid heading type")

def text_to_children(text) -> list[HTMLNode] | None:
    text_node = TextNode(text, TextType.PLAIN_TEXT)
    textnodes = text_to_textnodes([text_node])
    children = []
    for tn in textnodes:
        tn_html = text_node_to_html_node(tn)
        children.append(tn_html)
    return children

def clean_code_block(block) -> str:
    stripped = block.removeprefix("```\n").removesuffix("```")
    lines = stripped.split("\n")
    cleaned = ""
    for line in lines:
        cleaned += f"{line.strip()}\n"
    return cleaned.strip() + "\n"
