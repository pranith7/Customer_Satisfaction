import logging
from configs.logfile_configuration import get_console_logger


import pandas as pd 
from zenml import step


logging = get_console_logger(log_file_path=str(PARENT_DIR) + '/logs/system.log',name='model_evaluation')

@step 
def evaluate_model(df: pd.DataFrame) -> None:
    """
    Evaluates the model on the ingested data.

    Args:
       df: the ingested data
    """
    pass