from flask import Flask,request,Response
import json



app=Flask(__name__)

@app.route('/test',methods=['POST','GET'])
def preprocess():
    if request.method=='POST':
             data=request.get_json()
             c = data["course"]
             l = data["language"]
             t = data["topic"]
             res = '{'+'"Content":"{}"'.format(c+'-'+l+'-'+t)+'}'
             print(json.loads(res))
             return Response(json.dumps(json.loads(res)),mimetype='application/json')
             
if __name__=='__main__':
	app.run(host="0.0.0.0",port=8000)
