import logging

from logger_util import setup_logger
from utils.get_html_template import HTML_TEMPLATE_PATH

setup_logger()

logger = logging.getLogger(__name__)

from generate.generate_page import *
from generate.static_to_public import *

CONTENT_PATH = os.path.join(os.getcwd(), "content")


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

    generate_pages_recursively(CONTENT_PATH, HTML_TEMPLATE_PATH, PUBLIC_PATH)

if __name__ == "__main__":
    main()
