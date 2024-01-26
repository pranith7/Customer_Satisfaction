from pipelines.training_pipeline import train_pipeline
from zenml.client import Client
from utils.path import DATA_DIR , PARENT_DIR
DATA_DIR = str(DATA_DIR)
PARENT_DIR = str(PARENT_DIR)

if __name__ == "__main__":
    # print(Client().active_stack.experiment_tracker.get_tracking_uri())
    # print(DATA_DIR + "/olist_customers_dataset.csv")
    train_pipeline(data_path=str(DATA_DIR) + "/olist_customers_dataset.csv")

    
