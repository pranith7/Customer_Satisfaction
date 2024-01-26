import sys
sys.path.append("/teamspace/studios/this_studio/Customer_Satisfaction")
from utils.path import DATA_DIR , PARENT_DIR

import logging
from configs.logfile_configuration import get_console_logger
logging = get_console_logger(log_file_path=str(PARENT_DIR) + '/logs/system.log',name='model_training')

import pandas as pd 
from zenml import step

import mlflow
from src.model_dev import LinearRegressionModel
from sklearn.base import RegressorMixin
# from .config import ModelNameConfig
from configs.modelconfig import ModelNameConfig

# from zenml.client import Client
# experiment_tracker = Client().active_stack.experiment_tracker


@step
# @step(experiment_tracker=experiment_tracker.name)
def train_df(
    X_train: pd.DataFrame,
    X_test: pd.DataFrame,
    y_train: pd.DataFrame,
    y_test: pd.DataFrame,
    config: ModelNameConfig,
    ) -> RegressorMixin:
    """
    Trains the model on the ingested data
    
    Args:
        X_train: pd.DataFrame,
        X_test: pd.DataFrame,
        y_train: pd.DataFrame,
        y_test: pd.DataFrame,
    """
    try:
        model = None
        if config.model_name == "LinearRegression":
            # mlflow.sklearn.autolog()
            model = LinearRegressionModel()
            trained_model = model.train(X_train,y_train)
            return trained_model
        else:
            raise ValueError("Model {} not supported".format(config.model_name))
    except Exception as e:
        logging.error("Error in training model: {}".format(e))
        raise e
        