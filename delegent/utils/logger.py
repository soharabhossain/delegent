# logger.py

import logging
from functools import wraps
from user_config import ENABLE_LOGGING, LOG_FILE_PATH


logger = logging.getLogger("Delegent-Logger")
logger.setLevel(logging.INFO)

def get_logger(name: str = "delegent") -> logging.Logger:
    # Prevent duplicate handlers
    if not logger.handlers and ENABLE_LOGGING:
        file_handler = logging.FileHandler(LOG_FILE_PATH)
        console_handler = logging.StreamHandler()

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    return logger

def log_step(step_name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if ENABLE_LOGGING:
                logger.info(f" Starting: {step_name}")
            result = func(*args, **kwargs)
            if ENABLE_LOGGING:
                logger.info(f" Completed: {step_name}")
            return result
        return wrapper
    return decorator
