import pickle
from flask import Flask,request,render_template
import cv2,pandas as pd ,numpy as np
from src1.pipeline.predict_pipeline import PredictPipeline
#entry point
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_digit_img',methods=['GET'])
def predict_img():
    image = cv2.imread('mnist_images/mnist_7.png')
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

if __name__=="__main__":
    app.run(host="127.0.0.1") 