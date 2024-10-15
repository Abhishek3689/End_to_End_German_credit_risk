import yaml 
import pickle
from box import ConfigBox

def read_yaml(path):
    with open(path,'r') as f:
        return ConfigBox(yaml.safe_load(f))
    
def save_object(filepath,obj):
    with open(filepath, 'wb') as file_obj:
        pickle.dump(obj,file_obj)

config=read_yaml("config.yml")
azr_config=read_yaml("secrets.yml")