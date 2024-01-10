import logging
from configs.logfile_configuration import get_console_logger


import pandas as pd 
from zenml import step


logging = get_console_logger(log_file_path=str(PARENT_DIR) + '/logs/system.log',name='cleaning_data')

@step
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    pass