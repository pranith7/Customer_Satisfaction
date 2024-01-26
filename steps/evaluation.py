import sys
sys.path.append("/teamspace/studios/this_studio/Customer_Satisfaction")
from utils.path import DATA_DIR , PARENT_DIR


import logging
from configs.logfile_configuration import get_console_logger
logging = get_console_logger(log_file_path=str(PARENT_DIR) + '/logs/system.log',name='model_evaluation')



from zenml import step
import pandas as pd 
from src.evaluation import MSE,RMSE,R2

from sklearn.base import RegressorMixin
from typing import Tuple
from typing_extensions import Annotated
import mlflow

from zenml.client import Client
experiment_tracker = Client().active_stack.experiment_tracker


# @step(experiment_tracker=experiment_tracker.name)
@step
# @step(experiment_tracker=experiment_tracker.name)
def evaluate_model(model: RegressorMixin,
    X_test:pd.DataFrame,
    y_test:pd.DataFrame
    ) -> Tuple[
        Annotated[float,"r2_score"],
        Annotated[float,"rmse"],
    ]:

    """
    Evaluates the model on the ingested data.
    Args:
        df: the ingested data

    """
    try:
        prediction = model.predict(X_test)
        mse_class = MSE()
        mse = mse_class.calculate_scores(y_test,prediction)
      #   mlflow.log_metric("MSE", mse)

        r2_class = R2()
        r2 = r2_class.calculate_scores(y_test,prediction)
      #   mlflow.log_metric("R2", r2)

        rmse_class = RMSE()
        rmse = rmse_class.calculate_scores(y_test,prediction)
      #   mlflow.log_metric("RMSE", rmse)

        return r2, rmse

    except Exception as e:
        logging.error("Error in evaluating model: {}".format(e))
        raise e
