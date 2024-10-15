from src.components.data_ingest import DataIngestion
from src.components.data_transform import DataTransform
from src.utils import config
from src.logger import logging


if __name__=="__main__":
    data_ingestion=DataIngestion()
    train_path,test_path=data_ingestion.inititate_data_ingestion()
    logging.info(f"train path : {train_path} and test path :{test_path}")
    print(f"train path : {train_path} and test path :{test_path}")
    data_transform=DataTransform()
    train_arr,test_arr=data_transform.initiate_Data_Transformation(train_path,test_path)
    logging.info(f"train_array_shape :{train_arr.shape} | test array shape :{test_arr.shape}")
    print(f"train_array_shape :{train_arr.shape} | test array shape :{test_arr.shape}")

