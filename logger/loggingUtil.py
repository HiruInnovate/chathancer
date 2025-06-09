import logging
import os
from logging.handlers import RotatingFileHandler
from pathlib import Path


def get_logger(name: str, log_file: str = "app.log", level=logging.INFO) -> logging.Logger:
    logger_name = Path(name).stem
    log_path = os.path.join("logs", log_file)
    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    # Clear old handlers only if present
    if logger.hasHandlers():
        logger.handlers.clear()

    # File Handler
    file_handler = RotatingFileHandler(log_path, maxBytes=5 * 1024 * 1024, backupCount=5)
    file_handler.setLevel(level)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    # Formatter
    formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
