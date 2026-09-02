"""
src/generate/generate_page.py

This module provides a function to generate an HTML page from HTML template Markdown content.
"""
import logging

logger = logging.getLogger(__name__)
from fs_functions.path_utils import *
from utils.extract_title import extract_title
from utils.get_html_template import get_html_template
from utils.get_markdown_content_from_index import get_markdown_content
from utils.markdown_to_html_node import *


def generate_page(from_path: str, template_path:str, dest_path:str):
    html_template = get_html_template(template_path)
    markdown_content = get_markdown_content(from_path)
    title = extract_title(markdown_content)
    md_to_html = markdown_to_html_node(markdown_content)
    html = md_to_html.to_html()

    page_with_title = html_template.replace("{{ Title }}", title)
    page = page_with_title.replace("{{ Content }}", html)

    logger.info(f"Generating page from {from_path} to {dest_path}")
    write_page(page, dest_path)
    logger.info("New page generated. Start your server to view it in your browser at http://localhost:8888.")



def write_page(page:str, dest_path:str):
    with open(dest_path, "w") as f:
        f.write(page)

