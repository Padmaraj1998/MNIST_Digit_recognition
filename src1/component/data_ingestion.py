
import sys, os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ''))
sys.path.append(project_root)
from src1.exception import CustomException
from src1.logger import logging
from dataclasses import dataclass
import numpy as np
import pandas as pd

import tensorflow as tf

from src1.component.data_transformation import DataTransformation

@dataclass
class Data_ingestion_config:
    current_directory = os.getcwd()
    train_data_path = os.path.join(current_directory,"artifact","train_data.csv")
    test_data_path = os.path.join(current_directory,"artifact","test_data.csv")

class Data_ingestion_collection:
    def __init__(self):
        self.ingestion_config_capture = Data_ingestion_config()
    
    def data_ingestion_method(self):
        try:
            train_raw_data = pd.read_csv("dataset/mnist_train.csv")
            test_raw_data = pd.read_csv("dataset/mnist_test.csv")
            logging.info("Raw  data is read")
            
            #if create directory if doesnot exist
            os.makedirs(os.path.dirname(self.ingestion_config_capture.train_data_path),exist_ok=True)
            
            train_raw_data.to_csv(self.ingestion_config_capture.train_data_path,index=False,header=True)
            test_raw_data.to_csv(self.ingestion_config_capture.test_data_path,index=False,header=True)
            logging.info("Raw data file captured into artifact directory")
            return(self.ingestion_config_capture.train_data_path,self.ingestion_config_capture.test_data_path)
           
        except Exception as e:
            raise CustomException(e,sys)

if __name__ == "__main__":
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
    data_ingestion = Data_ingestion_collection()
    train_data,test_data = data_ingestion.data_ingestion_method()
    logging.info("Ingestion main class data captured")
    transformation = DataTransformation()
    transformation.transform_data(train_data,test_data)
