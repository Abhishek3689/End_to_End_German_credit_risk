import pandas as pd
import os,sys
from src.logger import logging
from src.exception import CustomException
from src.utils import evaluation,config,save_object
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier,GradientBoostingClassifier
from sklearn.svm import SVC
from dataclasses import dataclass
from pathlib import Path



models={
    "RandomForest":RandomForestClassifier(),
    "Adaboost":AdaBoostClassifier(),
    "SVM":SVC(),
    "Gradientboost":GradientBoostingClassifier()
}

@dataclass
class Model_trainer_Config:
    model_path:Path=os.path.join(config.model_trainer.model_path,"model.pkl")

class Modeltrainer:
    def __init__(self):
        self.model_config=Model_trainer_Config()

    def initiate_model_training(self,train_array,test_array):
        try:
            logging.info("Model Training Started !!!!!!")
            X_train_features=train_array[:,:-1]
            y_target_train=train_array[:,-1]
            X_test_features=test_array[:,:-1]
            y_target_test=test_array[:,-1]
            logging.info("Data has been splitted into input and output features using indexing for feeding to model")

            logging.info("Evaluating different algorithm Models ")

            try:
                reports=evaluation(models,X_train_features,X_test_features,y_target_train,y_target_test)
            except Exception as e:
                raise CustomException(e,sys)
            
            logging.info("Evaluation Done . Next step to find best models and score ")
            best_score_model=max(reports.items(),key=lambda x:x[1])
            logging.info(f"best model is {best_score_model[0]} and best score is {best_score_model[1]}")
            best_model_algorithm=models[list(best_score_model)[0]]

            logging.info("Saving the best model ")
            try:
                save_object(self.model_config.model_path,best_model_algorithm)  
            except Exception as e:
                raise CustomException(e,sys)
            logging.info("Model trainer Stage Completed")

        except Exception as e:
            raise CustomException(e,sys)
        
