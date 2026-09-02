from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    H1 = "h1"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block: str) -> BlockType:
    if is_block_heading(block):
        if is_block_h1(block):
            return BlockType.H1
        return BlockType.HEADING
    if is_code_block(block):
        return BlockType.CODE
    if is_quote_block(block):
        return BlockType.QUOTE
    if is_unordered_list(block):
        return BlockType.UNORDERED_LIST
    if is_ordered_list(block):
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def is_block_heading(block: str) -> bool:
    num_hash = len(block) - len(block.lstrip("#"))
    return 0 < num_hash <= 6 and block[num_hash:num_hash + 1] == " "

def is_block_h1(block: str) -> bool:
    return block.startswith("# ")

def is_code_block(block: str) -> bool:
    backticks_front = block.startswith("```\n")
    backticks_end = block.endswith("```")
    return backticks_front and backticks_end

def is_quote_block(block: str) -> bool:
    blocks = block.split("\n")
    def is_quote_block_inner(block_split: list[str]) -> bool:
        for b in block_split:
            if not b.startswith(">"):
                return False
        return True
    return is_quote_block_inner(blocks)

def is_unordered_list(block: str) -> bool:
    blocks = block.split("\n")
    def is_unordered_list_inner(block_split: list[str]) -> bool:
        for b in block_split:
            if not b.startswith("- "):
                return False
        return True
    return is_unordered_list_inner(blocks)

def is_ordered_list(block: str) -> bool:
    blocks = block.split("\n")
    def is_ordered_list_inner(block_split: list[str]) -> bool:
        number = 1
        for line in block_split:
            if line.startswith(f"{number}. "):
                number += 1
            else:
                return False
        return True
    return is_ordered_list_inner(blocks)
