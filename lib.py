""" library of shared code"""

import logging

def get_logger():
    """function to build a logger object.
    
    :returns: logger object 

    """

    logger = logging.getLogger(__name__)

    # Build stream output formatter
    stream_formatter = logging.Formatter("%(filename)s | %(funcName)s | "
                                    "%(lineno)d | %(levelname)s | "
                                    "%(message)s")

    # Build stream handler (for output to stdout)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel("DEBUG")
    stream_handler.setFormatter(stream_formatter)

    # Add handler to logger
    logger.addHandler(stream_handler)
    return logger

