"""
src/fs_functions/path_constants.py
Definitions for public/ and static/ paths
"""
import os

public_dir = os.path.join(os.getcwd(), "public")
static_dir = os.path.join(os.getcwd(), "static")

PUBLIC_PATH = public_dir
STATIC_PATH = static_dir