import sys
sys.path.append("/teamspace/studios/this_studio/Customer_Satisfaction")

from zenml import pipeline


from configs.logfile_configuration import get_console_logger
from utils.path import DATA_DIR , PARENT_DIR

from steps.ingest_data import ingest_df
from steps.clean_data import clean_df
from steps.model_train import train_df 
from steps.evaluation import evaluate_model




@pipeline()
def train_pipeline(data_path: str):
    df = ingest_df(data_path)
    clean_df(df)
    train_df(df)
    evaluate_model(df)