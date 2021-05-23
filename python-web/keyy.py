#!/usr/local/bin/python3.6

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/search', methods=['POST', 'GET'])
def home():
    if request.method == 'GET':
        data = request.args.get('q')  # request.args['q']
        print(data)
        res = {}
        res["Name"] = data
        res["Class"] = "MSME ML Deployment"
        return jsonify(res)

             
if __name__ == '__main__':
    app.run(port=8000)
    

