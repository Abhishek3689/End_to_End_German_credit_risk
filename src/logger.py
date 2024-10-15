import os
import logging
from datetime import datetime

filename=f"{datetime.now().strftime('%d-%m-%Y %H_%M_%S')}.logs"
log_folder='logs'
os.makedirs(log_folder,exist_ok=True)
file_path_name=os.path.join(log_folder,filename)

logging.basicConfig(
    filename=file_path_name,
    level=logging.INFO,
    format="[%(asctime)s -%(levelname)s] %(message)s"
)