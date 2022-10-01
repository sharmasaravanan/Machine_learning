import cv2
import numpy as np
from flask import Flask, request, render_template
import tensorflow as tf
from tensorflow.keras.models import load_model

model = load_model("mnistModel.mdl")
app = Flask(__name__)


def data_process(imgPath):
    img = cv2.imread(imgPath,0)
    invert = cv2.bitwise_not(img)
    testImg = cv2.resize(invert, (28,28)).reshape(1, 784)
    testImg = testImg.astype('float') / 255
    return testImg


@app.route('/', methods=['POST', 'GET'])
def predict_data():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        f = request.files['file']  
        f.save("test.png")  
        img = data_process("test.png")
        className = model.predict(img)
        kwarg = {"result": f"The predicted class is {np.argmax(className)} with score {np.max(className)}"}
        return render_template("index.html", **kwarg)


if __name__ == '__main__':
    app.run("0.0.0.0", port=5005)
