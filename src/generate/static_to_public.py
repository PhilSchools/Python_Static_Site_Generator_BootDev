import logging

logger = logging.getLogger(__name__)

from fs_functions.path_utils import *


def copy_static_to_public(path: str, contents: list[str]):
    for file in contents:
        file_path = get_full_path(path, file)
        if is_file(file_path):
            split_path = file_path.split(STATIC_PATH)
            public_join = get_full_path(PUBLIC_PATH, split_path[1].lstrip("/"))
            copy_file(file_path, public_join)
            logger.info(f"File copied: {file_path} to {public_join}")
        elif is_dir(file_path):
            contents = get_dir_contents(file_path)
            split_path = file_path.split(STATIC_PATH)
            public_join = get_full_path(PUBLIC_PATH, split_path[1].lstrip("/"))

            make_directory(public_join)
            logger.info(f"Directory created: {public_join}")
            copy_static_to_public(file_path, contents)

def clean_and_recreate_public():
    if public_path_exists():
        delete_public_dir()
        recreate_public_dir()
        logger.info("Public directory cleaned and recreated")
    else:
        recreate_public_dir()
        logger.info("Public directory did not exist, but has been recreated")
    public_contents = get_public_dir_contents()
    logger.info(f"Public directory contents: {public_contents}")



