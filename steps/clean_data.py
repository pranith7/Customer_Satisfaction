import sys
sys.path.append("/teamspace/studios/this_studio/Customer_Satisfaction")

import logging
from configs.logfile_configuration import get_console_logger


import pandas as pd 
from zenml import step

from utils.path import DATA_DIR , PARENT_DIR

logging = get_console_logger(log_file_path=str(PARENT_DIR) + '/logs/system.log',name='cleaning_data')

@step
def clean_df(df: pd.DataFrame) -> None:
    pass