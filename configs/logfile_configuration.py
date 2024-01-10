import logging
from typing import Optional
from datetime import datetime
import pytz

def get_console_logger(log_file_path: Optional[str] = 'logfile.log', name: Optional[str] = 'tutorial') -> logging.Logger:
    # Create logger if it doesn't exist
    logger = logging.getLogger(name)

    if not logger.handlers:
        # Set the logging level to DEBUG
        logger.setLevel(logging.DEBUG)

        # Create console handler with formatting
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        # Set the time zone explicitly when creating the formatter
        ist = pytz.timezone('Asia/Kolkata')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S IST')
        formatter.converter = lambda *args: datetime.now(ist).timetuple()

        console_handler.setFormatter(formatter)

        # Create file handler with formatting
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        # Add both handlers to the logger
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger