import logging
import os
import sys


def setup_logger(name=None):
    """
    Configure the root logger and return a logger instance.
    Initialize in main.py before other modules are imported.
    :param name:
    :return:
    """

    logger = logging.getLogger(name)

    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    log_format = logging.Formatter(
        fmt='%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s',
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    console_handler = logging.StreamHandler(sys.stdout)

    console_handler.setFormatter(log_format)

    console_handler.terminator = '\n\n'

    logger.addHandler(console_handler)

    file_handler = logging.FileHandler(os.path.join(os.getcwd(), 'logs', 'app.log'), mode='w')

    file_handler.setFormatter(log_format)

    file_handler.terminator = '\n\n'

    logger.addHandler(file_handler)

    return logger