import os,sys,pandas as pd,numpy as np
from dataclasses import dataclass
from src1.exception import CustomException
import keras

@dataclass
class Model_Trainer_Config:
    curr_dir = os.getcwd()
    model_trainer_pkl_path = os.path.join(curr_dir,"artifact","model_trainer.pkl")

class Model_Trainer:
    def __init__(self):
        self.model_trainer_config = Model_Trainer_Config()
    def train_model(self,train_array,test_array):
        try:
            X_train,Y_train,X_test,Y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            #flatten - dimension of data and type of image, i have given grayscale
            # if rgb needed then (28,28,3)
            #dense is 10 - due to 0-9 output
            model = keras.Sequential([
                keras.layers.Input(shape=(784,)),  # Define input shape with Input layer
                keras.layers.Flatten(),
                keras.layers.Dense(50, activation="relu"),
                keras.layers.Dense(55, activation="relu"),
                keras.layers.Dense(10, activation="sigmoid")
            ])

            model.compile(optimizer="adam",loss="sparse_categorical_crossentropy",metrics=['accuracy'])
            #train the data
            model.fit(X_train,Y_train,epochs=10)
            #accuracy of test data
            loss,accuracy = model.evaluate(X_test,Y_test)
            print(accuracy)
            return 0
        except Exception as e:
            raise CustomException(e,sys)