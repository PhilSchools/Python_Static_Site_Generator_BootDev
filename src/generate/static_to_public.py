import logging

logger = logging.getLogger(__name__)

from fs_functions.path_utils import *


def copy_static_to_dest(static_path: str, contents: list[str], dest_path: str):
    for file in contents:
        file_path = get_full_path(static_path, file)
        if is_file(file_path):
            split_path = file_path.split(STATIC_PATH)
            dest_join = get_full_path(dest_path, split_path[1].lstrip("/"))
            copy_file(file_path, dest_join)
            logger.info(f"File copied: {file_path} to {dest_join}")
        elif is_dir(file_path):
            contents = get_dir_contents(file_path)
            split_path = file_path.split(STATIC_PATH)
            dest_join = get_full_path(dest_path, split_path[1].lstrip("/"))

            make_directory(dest_join)
            logger.info(f"Directory created: {dest_join}")
            copy_static_to_dest(file_path, contents, dest_path)

def clean_and_recreate_dest(dest_path: str):
    if path_exists(dest_path):
        delete_dir(dest_path)
        recreate_dir(dest_path)
        logger.info(f"{dest_path} directory cleaned and recreated")
    else:
        recreate_dir(dest_path)
        logger.info(f"{dest_path} directory did not exist, but has been recreated")
    dir_contents = get_dir_contents(dest_path)
    logger.info(f"{dest_path} directory contents: {dir_contents}")



