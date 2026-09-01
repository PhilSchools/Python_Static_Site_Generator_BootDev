import logging

from logger_util import setup_logger

setup_logger()

logger = logging.getLogger(__name__)

from generate.static_to_public import *


def main():
    clean_and_recreate_public()
    logger.info("MAIN: Public directory deleted and recreated")
    static_contents = get_static_dir_contents()
    logger.info(f"MAIN: Calling copy_static_to_public with \n"
                f"STATIC_PATH: {STATIC_PATH} and Static directory contents: \n"
                f" {static_contents}")
    copy_static_to_public(STATIC_PATH, static_contents)
    logger.info("MAIN: Static files copied to public directory")
    logger.info("MAIN: Public directory contents: ")
    logger.info(f"MAIN: {get_public_dir_contents()}")
    logger.info("MAIN: Done")


if __name__ == "__main__":
    main()
