from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def home():
    print(request)
    if request.method == 'GET':
        print(request)
        q = request.args['q']
        response = {'Name': q, "Number": 123}
        return jsonify(response)


if __name__ == '__main__':
    app.run()
