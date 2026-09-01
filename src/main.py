from logger_util import setup_logger
import logging

setup_logger()

logger = logging.getLogger(__name__)

def main():
    logger.info("Application has started.")




if __name__ == "__main__":
    main()
