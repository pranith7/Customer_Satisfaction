import sys
sys.path.append("/teamspace/studios/this_studio/Customer_Satisfaction")

from typing import Optional
from pathlib import Path

import pandas as pd
import requests
import fire

from configs.logfile_configuration import get_console_logger
from utils.path import DATA_DIR , PARENT_DIR

logger = get_console_logger(log_file_path=str(PARENT_DIR) + '/logs/system.log',name='data_cleaning')

logger.info("info message")
logger.debug("debug message")
logger.error("error messaage")
logger.warning("warning message")
logger.critical("critical message")

