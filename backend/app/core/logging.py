"""
Centralized logging configuration for AKRAS.
"""

import logging
import sys


def setup_logger(name: str = "AKRAS") -> logging.Logger:
    """
    Create and configure an application logger.

    Args:
        name: Logger name.

    Returns:
        Configured logger instance.
    """

    logger = logging.getLogger(name)

    if logger.hasHandlers():
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger


logger = setup_logger()