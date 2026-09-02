"""
src/utils/get_html_template.py

This module provides a function to extract HTML template from template.html.
"""
import os

HTML_TEMPLATE = "template.html"
HTML_TEMPLATE_PATH = os.path.join(os.getcwd(), HTML_TEMPLATE)

def get_html_template(file=HTML_TEMPLATE_PATH):
    with open(file, "r") as f:
        return f.read()
