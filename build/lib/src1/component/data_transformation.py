from dataclasses import dataclass
import os,sys,pandas as pd,numpy as np
from src1.logger import logging
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from src1.utils import save_object

@dataclass
class DataTransformationconfig:
    current_directory = os.getcwd()
    preprocessor_obj_file = os.path.join(current_directory,"artifact","preprocessor.pkl")
    logging.info(f"pickle file location -  {preprocessor_obj_file}")

class DataTransformation:
    def __init__(self):
        self.data_transformation = DataTransformationconfig()
    def preprocessing(self):
        nums_cols = list(range(0, 784))
        num_pipeline = Pipeline(
            steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scalar", StandardScaler())
                ]
            )
        preprocessor = ColumnTransformer(
            [
                ("num_pipeline",num_pipeline,nums_cols)
                    
            ]
        )
        return preprocessor
    def transform_data(self,train_path,test_path):
        train_df = pd.read_csv(train_path)
        test_df = pd.read_csv(test_path)

        preprocessor_obj = self.preprocessing()

        target_col_name = "0"
       
        input_feature_train_df = train_df.drop(columns=[target_col_name],axis=1)
        target_feature_train_df = train_df[target_col_name]

        input_feature_test_df = test_df.drop(columns=[target_col_name],axis=1)
        target_feature_test_df = test_df[target_col_name]
        logging.info(f"Applying preprocessing object on training dataframe and testing dataframe")
        
       

        input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
        input_feature_test_arr  = preprocessor_obj.transform(input_feature_test_df)
        

        # # Reshape the training data from (60000, 784) to (60000, 28, 28)
        # input_feature_train_reshaped = input_feature_train_arr.reshape(-1,28, 28)
        # input_feature_test_reshaped = input_feature_test_arr.reshape(-1,28, 28)

        
        # After preprocessing concatenate column wise with transformed data and targeted data
        train_arr = np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
        test_arr = np.c_[input_feature_test_arr,np.array(target_feature_test_df)]
        
        save_object(
            self.data_transformation.preprocessor_obj_file,
            preprocessor_obj
        )

        logging.info("Saved preprocessing object")

        return(
            train_arr,
            test_arr
        )