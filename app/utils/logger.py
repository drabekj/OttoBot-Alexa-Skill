import logging

import os

logger = logging.getLogger(__name__)

# define the default level of the logger.
# We could specify a greater (LESS VERBOSE) level on the single handler
logger.setLevel(logging.DEBUG)

# creating a formatter.
# to see all the attributes you can use
FORMAT = "%(asctime)s | %(levelname)s | %(filename)s:%(lineno)s - %(funcName)20s() | -> %(message)s"
formatter = logging.Formatter(FORMAT)

# creating a handler to log on the filesystem
LOGS_DIR = os.path.join(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'logs')
file_handler = logging.FileHandler(LOGS_DIR + '/dev.log', encoding="UTF-8")
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)
# creating a handler to log on the console
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.DEBUG)

# adding handlers to our logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)
