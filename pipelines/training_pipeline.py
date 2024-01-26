import sys
sys.path.append("/teamspace/studios/this_studio/Customer_Satisfaction")

from configs.logfile_configuration import get_console_logger
from utils.path import DATA_DIR , PARENT_DIR




from zenml import pipeline
from steps.ingest_data import ingest_df
from steps.clean_data import clean_df
from steps.model_train import train_df 
from steps.evaluation import evaluate_model

@pipeline(enable_cache=True)
def train_pipeline(data_path: str):
     df = ingest_df(data_path)
     X_train,X_test,y_train, y_test = clean_df(df)
     model = train_df(X_train,X_test,y_train,y_test) 
     r2_score,rmse = evaluate_model(model,X_test,y_test)





