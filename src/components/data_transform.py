import os,sys
from src.utils import config,save_object
from src.logger import logging
from src.exception import CustomException
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler,OneHotEncoder,OrdinalEncoder
from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataTransformConfig:
    preprocessor_path:Path=os.path.join(config.data_transform.preprocessor_path,"preprocessor.pkl")


def get_data_transform_object():
    try:
        logging.info("Process started to get preprocessor object ")
        cat_col_ohe=['Sex', 'Housing', 'Purpose']
        cat_col_ord=['Saving accounts', 'Checking account',]
        num_col=['Age', 'Job', 'Credit amount','Duration']

        logging.info("Building Pipeline for preprocessor")
        cat_pipeline_ohe=Pipeline([
        ("imputer",SimpleImputer(strategy='most_frequent')),
        ('encoder',OneHotEncoder())
        ])
        cat_pipeline_ord=Pipeline([
            ("imputer",SimpleImputer(strategy='most_frequent')),
            ('encoder',OrdinalEncoder())
        ])
        num_pipeline=Pipeline([
            ('imputer',SimpleImputer(strategy='median')),
            ('scaler',StandardScaler())
        ])

        logging.info("Creating Preprocessor Object")
        preprocessor=ColumnTransformer([
            ("Cateory1",cat_pipeline_ohe,cat_col_ohe),
            ("Category2",cat_pipeline_ord,cat_col_ord),
            ('Numercial',num_pipeline,num_col)
        ])
        logging.info("Preprocessor built and returned")
        return preprocessor
    
    except Exception as e:
        raise CustomException(e,sys)
    
class DataTransform:
    def __init__(self):
        self.data_transform_config=DataTransformConfig()

    def initiate_Data_Transformation(self,train_path,test_path):
        try:
            logging.info("Data Transformation Initiated ")
            os.makedirs(os.path.dirname(self.data_transform_config.preprocessor_path),exist_ok=True)

            preprocessor=get_data_transform_object()

            logging.info("Loading train and test data and segregating dependent and independent features")
            train_data=pd.read_csv(train_path,index_col=0)
            logging.info(f"trin data shape {train_data.shape} and type is {type(train_data)} and columns are [{train_data.columns}]")
            train_features=train_data.drop(columns=['Risk'],axis=1)
            
            # train_features=train_data.drop(['Risk','Unnamed: 0'],axis=1)
            traget_column="Risk"
            train_target=train_data['Risk'].map({'good': 1, 'bad': 0})

            test_data=pd.read_csv(test_path,index_col=0)
            test_features=test_data.drop(columns=['Risk'],axis=1)
            # test_data=test_data['Risk'].map({'good':1,'bad':0})
            # test_features=test_data.drop(['Risk','Unnamed: 0'],axis=1)
            test_target=test_data['Risk'].map({'good': 1, 'bad': 0})

            logging.info("Scaling the input train and test features ")
            logging.info(f"train column 2 :{train_data.columns[2]}")
            train_features_scaled=preprocessor.fit_transform(train_features)
            test_features_scaled=preprocessor.transform(test_features)

            logging.info("merging the input and oput features together after scaling")
            train_features_scaled=np.c_[train_features_scaled,train_target]
            test_features_scaled=np.c_[test_features_scaled,test_target]

            logging.info("Saving the preprocssor model")
            try:
                save_object(self.data_transform_config.preprocessor_path,preprocessor)
            except Exception as e:
                raise CustomException(e,sys)
            logging.info("Data Transformation completed ")
            return(
                train_features_scaled,
                test_features_scaled
            )
        
        except Exception as e:
            logging.error(f"An error occurred during data itransformation: {e}")
            raise CustomException(e,sys)
