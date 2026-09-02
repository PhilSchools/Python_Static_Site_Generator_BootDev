import logging
import os

from logger_util import setup_logger
from utils.get_html_template import HTML_TEMPLATE_PATH
from utils.get_markdown_content_from_index import MARKDOWN_INDEX_PATH

setup_logger()

logger = logging.getLogger(__name__)

from generate.generate_page import *
from generate.static_to_public import *


def main():
    logger.info("Starting the application. Generating static files...")
    logger.info("Cleaning and recreating the public directory")
    clean_and_recreate_public()

    static_files = get_static_dir_contents()
    if public_path_exists():
        copy_static_to_public(STATIC_PATH, static_files)
    else:
        logger.error("Public path does not exist. Attempting to recreate.")
        recreate_public_dir()
        copy_static_to_public(STATIC_PATH, static_files)

    template_path = HTML_TEMPLATE_PATH
    from_path = MARKDOWN_INDEX_PATH
    to_path = os.path.join(PUBLIC_PATH, "index.html")

    generate_page(from_path, template_path, to_path)

    if is_file(to_path):
        logger.info(f"Generated page successfully at {to_path}")
    else:
        logger.error("Failed to generate page")


if __name__ == "__main__":
    main()
