import pickle,os,sys
from flask import Flask,request,render_template
import cv2,pandas as pd ,numpy as np
from src1.pipeline.predict_pipeline import PredictPipeline
from src1.logger import logging
from src1.exception import CustomException
#entry point
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_digit_img',methods=['GET','POST'])
def predict_img():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            upload_file_path = os.path.join(os.getcwd(), "Uploaded_Img")
            os.makedirs(upload_file_path,exist_ok=True)
            
            if 'image' not in request.files:
                return render_template('home.html',results="File does not exits")
            file = request.files['image']
            print(f"filename:{file.filename}")
            if file.filename == '':
                return render_template('home.html',results="File does not exits")
            if file:
                file_path = os.path.join(upload_file_path,file.filename)
                file.save(file_path)
                logging.info("File saved successfully")
            image = cv2.imread(file_path)
            # image = cv2.imread('mnist_images/mnist_7.png')
            #convert RGB to Gray scale image
            grayscale = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
            #resize image size to 28,28
            image_resize = cv2.resize(grayscale,(28,28))
            #reshape to 784
            image_reshape = image_resize.reshape(1,784)

            print("Before Prediction")

            predict_pipeline=PredictPipeline()
            print("Mid Prediction")
            probability = predict_pipeline.predict(image_reshape)
            results = np.argmax(probability)

            print("after Prediction")
            return render_template('home.html',results=results)
        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    app.run(host="127.0.0.1") 