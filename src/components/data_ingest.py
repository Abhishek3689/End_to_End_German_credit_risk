import yaml
from src.logger import logging
from src.exception import CustomException
import os,sys
from src.utils import config,   get_azure_connection_string
from dataclasses import dataclass
from azure.storage.blob import BlobClient
import pandas as pd
from sklearn.model_selection import train_test_split
from pathlib import Path


@dataclass
class DataIngestionConfig:
   
    raw_path:Path =  config.data_ingestion.raw_path 

    train_path:Path = config.data_ingestion.train_path
    test_path:Path =  config.data_ingestion.test_path

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()

    def inititate_data_ingestion(self):
       
        try:
            logging.info("Data Ingestion Started")
            logging.info("Connecting with the Azure blob")

            blob = BlobClient.from_connection_string(
                conn_str=get_azure_connection_string(),
                container_name=config.container_name, 
                blob_name=config.blob_name
            )
            logging.info("Connection successful")

            os.makedirs(self.data_ingestion_config.raw_path, exist_ok=True)
            raw_filepath = os.path.join(self.data_ingestion_config.raw_path, "German_credit.csv")
            logging.info(f"Raw file path: {raw_filepath}")

            logging.info("Loading the raw file from Azure storage")
            with open(raw_filepath, "wb") as my_blob:
                blob_data = blob.download_blob()
                data = blob_data.readall()
                my_blob.write(data)
                logging.info(f"Downloaded blob size: {len(data)} bytes")

            logging.info(f"Raw file has been saved at {raw_filepath}")

            # Load the raw data
            raw_data = pd.read_csv(raw_filepath)
            logging.info("Raw data loaded successfully.")
            logging.debug(f"First few rows of raw data: \n{raw_data.head().to_string()}")

            # Split the data
            train_data, test_data = train_test_split(raw_data, test_size=0.2, random_state=56)
            logging.info(f"Train data shape: {train_data.shape}, Test data shape: {test_data.shape}")

            # Define absolute paths for saving train and test data
            os.makedirs(self.data_ingestion_config.train_path, exist_ok=True)
            train_filepath = os.path.join(self.data_ingestion_config.train_path, "train.csv")
            os.makedirs(self.data_ingestion_config.test_path, exist_ok=True)
            test_filepath = os.path.join(self.data_ingestion_config.test_path, "test.csv")
            logging.info(f"train file path: {train_filepath} | test file path :{test_filepath}")

          
            # # Ensure directories exist
            # os.makedirs(os.path.dirname(train_csv_path), exist_ok=True)
            # os.makedirs(os.path.dirname(test_csv_path), exist_ok=True)

            # Save train and test data to CSV
            train_data.to_csv(train_filepath, index=False, header=True)
            test_data.to_csv(test_filepath, index=False, header=True)

            logging.info(f"Train data saved at: {train_filepath}")
            logging.info(f"Test data saved at: {test_filepath}")


            logging.info("Train and test data are saved in destination")
            df_test=pd.read_csv(test_filepath)
            print(df_test.head())


            return (
                train_filepath,
                test_filepath
            )
        except Exception as e:
            logging.error(f"An error occurred during data ingestion: {e}")
            raise CustomException(e, sys)


