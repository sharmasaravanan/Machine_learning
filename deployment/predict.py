#! /usr/local/bin/python3.6

# importing lib
import json
import pickle
from flask import Flask, request, Response, jsonify

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def prediction():
    if request.method == "POST":
        data = request.get_json()
        sales = model.predict([data['investAmount']])
        resp = {"sales": sales[0]}
        return jsonify(resp)

if __name__ == '__main__':
    fileName = "LR_API.model"
    model = pickle.load(open(fileName,'rb'))
    app.run(host="0.0.0.0", port=5001)