import os,sys
import pandas as pd
from src1.exception import CustomException
from src1.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            current_directory = os.getcwd()
            model_path=os.path.join(current_directory,"artifact","model_trainer.pkl")
            preprocessor_path=os.path.join(current_directory,'artifact','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)