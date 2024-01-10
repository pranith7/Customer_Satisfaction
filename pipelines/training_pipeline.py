from zenml import pipeline

from utils.path import DATA_DIR , PARENT_DIR
DATA_DIR = str(DATA_DIR)
PARENT_DIR = str(PARENT_DIR)

print(PARENT_DIR)

from steps.ingest_data import ingest_df
from steps.clean_data import clean_df
from steps.model_train import train_df 
from steps.evaluation import evaluate_model




# @pipelines()
# def train_pipeline(data_path: str):
#     df = ingest_df(data_path)
#     clean_df(df)
#     train_df(df)
#     evaluate_model(df)