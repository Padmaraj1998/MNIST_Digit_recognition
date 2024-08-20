import os
from datetime import datetime 
import logging

file_name = f"{datetime.now().strftime('%m_%d_%Y_%H')}.log"
file_path = os.path.join(os.getcwd(),'logs')
LOG_FILE = os.makedirs(file_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(file_path,file_name)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__=="__main__":
    logging.info("logging has started")