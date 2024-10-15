import yaml 
import pickle
from box import ConfigBox
from sklearn.metrics import accuracy_score,confusion_matrix

def read_yaml(path):
    with open(path,'r') as f:
        return ConfigBox(yaml.safe_load(f))
    
def save_object(filepath,obj):
    with open(filepath, 'wb') as file_obj:
        pickle.dump(obj,file_obj)

def evaluation(models,X_train,X_test,y_train,y_test):
    report={}
    for i in range(len(models)):
    
        model=list(models.values())[i]
        model.fit(X_train,y_train)
        y_pred=model.predict(X_test)
        score=accuracy_score(y_test,y_pred)
        cf=confusion_matrix(y_test,y_pred)
        print(f"confusion matrix for model {model}: {cf}")
        report[list(models.keys())[i]]=score
    return report 

def load_object(filepath):
    with open(filepath,'rb') as file_obj:
        return pickle.load(file_obj) 

config=read_yaml("config.yml")
azr_config=read_yaml("secrets.yml")