"""
src/generate/generate_page.py

This module provides a function to generate an HTML page from HTML template Markdown content.
"""
import logging

from main import CONTENT_PATH

logger = logging.getLogger(__name__)
import pathlib

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

def generate_pages_recursively(dir_path_content: str, template_path: str, dest_dir_path: str):
    tp = template_path

    walked = pathlib.Path(dir_path_content).walk()
    for root, dirs, files in walked:
        if files:

            for file in files:
                rp = root.relative_to(dir_path_content)


                file_path = (get_full_path(rp, file)).rstrip("/.").lstrip("./")
                from_path = get_full_path(CONTENT_PATH, file_path)
                dest_path = get_full_path(dest_dir_path, file_path).replace(".md", ".html")
                dest_dir = get_full_path(PUBLIC_PATH, rp)
                logger.info(f"\n\nGenerating Page Details: \n"
                            f"\nShort Root: {rp}, \n"
                            f"Template Path: {template_path}, \n"
                            f"File: {file}, \n"
                            f"File Path: {file_path}, \n"
                            f"From Path: {from_path}, \n"
                            f"Dest Dir:{dest_dir} \n"
                            f"Dest Path:{dest_path} \n\n")
                if not is_dir(dest_dir):
                    os.makedirs(dest_dir)
                    logger.info(f"Directory created: {dest_dir}")
                generate_page(from_path, tp, dest_path)

def write_page(page:str, dest_path:str):
    with open(dest_path, "w") as f:
        f.write(page)

