import json

from flask import Flask, request, Response, jsonify

app=Flask(__name__)

@app.route('/test',methods=['POST','GET'])
def preprocess():
    if request.method == "GET":
        resp = {"status": "SUCCESS", "error": " "}
        return jsonify(resp)
    elif request.method == 'POST':
             data=request.get_json()
             c = data["course"]
             l = data["language"]
             t = data["topic"]
             res = '{'+'"Content":"{}"'.format(c+'-'+l+'-'+t)+'}'
             return Response(json.dumps(json.loads(res)),mimetype='application/json')
             
if __name__=='__main__':
    app.run()
