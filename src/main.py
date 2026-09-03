import logging
import sys

from logger_util import setup_logger
from utils.get_html_template import HTML_TEMPLATE_PATH

setup_logger()

logger = logging.getLogger(__name__)

from generate.generate_page import *
from generate.static_to_public import *

CONTENT_PATH = os.path.join(os.getcwd(), "content")
BASEPATH = sys.argv[1] if len(sys.argv) > 1 else "/"
DOCS_DIRECTORY = os.path.join(os.getcwd(), "docs")

def main():
    logger.info("Starting the application. Generating static files...")
    logger.info("Cleaning and recreating the public directory")
    clean_and_recreate_dest(DOCS_DIRECTORY)
    static_files = get_static_dir_contents()

    if path_exists(DOCS_DIRECTORY):
        copy_static_to_dest(STATIC_PATH, static_files, DOCS_DIRECTORY)
    else:
        logger.error("Public path does not exist. Attempting to recreate.")
        recreate_dir(DOCS_DIRECTORY)
        copy_static_to_dest(STATIC_PATH, static_files, DOCS_DIRECTORY)

    generate_pages_recursively(CONTENT_PATH, HTML_TEMPLATE_PATH, DOCS_DIRECTORY, BASEPATH)

if __name__ == "__main__":
    main()
