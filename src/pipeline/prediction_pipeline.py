import os,sys
from src.utils import load_object
from src.utils import config
import pandas as pd
from src.components.model_trainer import Modeltrainer
from src.components.data_transform import DataTransform
from src.components.data_ingest import DataIngestion
from sklearn.metrics import accuracy_score,roc_auc_score

data_config=DataIngestion()
test_data_path=data_config.data_ingestion_config.test_path
test_data_path=os.path.join(test_data_path,"test.csv")

preprocessor_config=DataTransform()
preprocessor_path=preprocessor_config.data_transform_config.preprocessor_path

model_trainer=Modeltrainer()
model_path=model_trainer.model_config.model_path

model=load_object(model_path)
preprocessor=load_object(preprocessor_path)

df_test=pd.read_csv(test_data_path).iloc[:,1:]
print(df_test.head())

X_test=df_test.drop('Risk',axis=1)
y_test=df_test['Risk'].map({'good':1,'bad':0})
X_test_scaled=preprocessor.transform(X_test)
y_pred=model.predict(X_test_scaled)

print(f"accuracy score :{accuracy_score(y_pred,y_test)}")
print(f"roc auc score :{roc_auc_score(y_test,y_pred)}")