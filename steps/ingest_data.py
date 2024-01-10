import sys
sys.path.append("/teamspace/studios/this_studio/Customer_Satisfaction")

import logging
from configs.logfile_configuration import get_console_logger
import pandas as pd 
from zenml import step

from utils.path import DATA_DIR , PARENT_DIR

logging = get_console_logger(log_file_path=str(PARENT_DIR) + '/logs/system.log',name='ingesting_data')


class IngestData:
    """
     Ingesting the data from the data_path. 
    """
    def __init__(self,data_path:str):
        """
        Args:
            data_path: path to the data
        """
        self.data_path = data_path

    def get_data(self):
        """
         Ingesting the data from the data_path.
        """
        logging.info(f"Ingesting data from {self.data_path}")
        return pd.read_csv(self.data_path)


@step
def ingest_df(data_path:str) -> pd.DataFrame:
    """
    Ingesting the data from the data_path.

    Args:
        data_path: path to the data
    Returns:
        pd.DataFrame: the ingested data     
    """

    try:
        ingest_data = IngestData(data_path)
        df = ingest_data.get_data()
        return df
    except Exception as e:
        logging.error(f"Error while ingesting data {e}")
        raise e

        
