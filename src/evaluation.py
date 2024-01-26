import sys
sys.path.append("/teamspace/studios/this_studio/Customer_Satisfaction")
from utils.path import DATA_DIR , PARENT_DIR


import logging
from configs.logfile_configuration import get_console_logger
logging = get_console_logger(log_file_path=str(PARENT_DIR) + '/logs/system.log',name='model_evaluation')


from abc import ABC,abstractmethod
import numpy as np
from sklearn.metrics import r2_score,mean_squared_error

class Evaluation(ABC):
    """ 
    Abstract class definiing strategy for evaluation our models.
    """
    @abstractmethod
    def calculate_scores(self,y_true:np.ndarray,y_pred: np.array):
        """
        Calculates the scores for the model
        Args:
            y_true: True labels
            y_pred: Predicted labels
        Returns:
            None
        """
        pass


class MSE(Evaluation):
    """ 
    Evaluation Strategy that uses Mean Squared error.
    """

    def calculate_scores(self,y_true:np.ndarray,y_pred: np.array):
        try:
            logging.info("Calculating MSE")
            mse = mean_squared_error(y_true,y_pred)
            logging.info("MSE: {}".format(mse))
            return mse
        except Exception as e:
            logging.error("Error in calculating MSE: {}".format(e))
            raise e

class R2(Evaluation):
    """ 
    Evaluation Strategy that uses R2 score.
    """

    def calculate_scores(self,y_true:np.ndarray,y_pred: np.array):
        try:
            logging.info("Calculating R2 score")
            r2 = r2_score(y_true,y_pred)
            logging.info("R2 score: {}".format(r2))
            return r2
        except Exception as e:
            logging.error("Error in calculating R2 Score: {}".format(e))
            raise e

class RMSE(Evaluation):
    """ 
    Evaluation Strategy that uses Root Mean Squared error.
    """

    def calculate_scores(self,y_true:np.ndarray,y_pred: np.array):
        try:
            logging.info("Calculating RMSE")
            rmse = mean_squared_error(y_true,y_pred,squared=False)
            logging.info("RMSE: {}".format(rmse))
            return rmse
        except Exception as e:
            logging.error("Error in calculating RMSE: {}".format(e))
            raise e