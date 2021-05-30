import base64
import numpy as np
from PIL import Image
from flask import Flask, request, render_template
from tensorflow.keras.models import load_model

model = load_model('model.h5')


def data_process(data):
    data = np.array(data)
    data = data.reshape((1, 28, 28, 1))
    data = data.astype('float64') / 255
    return data


app = Flask(__name__)


@app.route('/predict', methods=['POST', 'GET'])
def predict_data():
    t = request.form['file']
    t = t[23:]
    image = base64.b64decode(t)
    path = "test.jpeg"
    file = open(path, 'wb')
    file.write(image)
    file.close()
    data = Image.open(path).convert('L')
    data = data.resize((28, 28))
    data = np.array(data, 'f')

    data = data_process(data)
    result = model.predict(data)
    return str(result.argmax())


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run("0.0.0.0", port=5005)
