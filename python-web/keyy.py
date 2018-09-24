from flask import Flask,request,jsonify #Django,cherrypy,bottle
import json

app=Flask(__name__)

@app.route('/python',methods=['POST','GET'])
def home():
    if request.method=='POST':
             #data=request.args.get('d')#request.args['q']
             data = request.values.get('fruit')
             print(data)
             res='{'+'"Name":"{}"'.format(data)+'}'
             print(json.loads(res))
             #return jsonify(res)
             return json.dumps(json.loads(res))
             
if __name__=='__main__':
	app.run(host="0.0.0.0",port=8000)
