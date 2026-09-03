"""
src/fs_functions/path_utils.py
Utilities for checking paths and directory contents
"""
import logging
import shutil

logger = logging.getLogger(__name__)

from fs_functions.path_constants import *


def public_path_exists():
    return os.path.exists(PUBLIC_PATH)

def path_exists(path):
    return os.path.exists(path)

def static_path_exists():
    return os.path.exists(STATIC_PATH)

def get_public_dir_contents():
    return os.listdir(PUBLIC_PATH)

def get_static_dir_contents():
    return os.listdir(STATIC_PATH)

def get_dir_contents(path: str):
    return os.listdir(path)

def is_dir(path, /):
    return os.path.isdir(path)

def is_file(path):
    return os.path.isfile(path)

def get_full_static_path_for_file(file):
    return os.path.join(STATIC_PATH, file)

def get_full_path(path, file):
    return os.path.join(path, file)

def recreate_public_dir():
    if not public_path_exists():
        os.mkdir(PUBLIC_PATH)

def recreate_dir(path: str):
    if not path_exists(path):
        os.mkdir(path)

def make_directory(path):
    if not is_dir(path):
        os.mkdir(path)

def copy_file(src, dst):
    shutil.copyfile(src, dst)

def delete_public_dir():
    shutil.rmtree(PUBLIC_PATH)

def delete_dir(path: str):
    shutil.rmtree(path)
