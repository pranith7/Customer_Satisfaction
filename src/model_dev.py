
import sys
sys.path.append("/teamspace/studios/this_studio/Customer_Satisfaction")
from utils.path import DATA_DIR , PARENT_DIR

import logging
from configs.logfile_configuration import get_console_logger
logging = get_console_logger(log_file_path=str(PARENT_DIR) + '/logs/system.log',name='cleaning_data')


from abc import ABC, abstractmethod
from sklearn.linear_model import LinearRegression

class Model(ABC):
    """
    Abstract class for all models 
    """
    @abstractmethod
    def train(self,X_train,y_train):
        """
        Trains the model
        Args:
            x_train: Training data
            y_train: Training labels
        Returns:
            None 
        """
        pass

class LinearRegressionModel(Model):
    """
    Linear Regression model 
    """
    def train(self,X_train,y_train,**kwargs):

        """
        Trains the model
        Args:
            X_train: Training data
            y_train: Training labels
        Returns:
            None 
        """
       
        try:
            reg = LinearRegression(**kwargs)
            reg.fit(X_train,y_train)
            logging.info("Model training Completed")
            return reg
        except Exception as e:
            logging.error("Error in handling data: {}".format(e))
            raise e
    
