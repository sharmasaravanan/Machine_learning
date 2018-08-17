from flask import Flask,request,jsonify #Django,cherrypy,bottle
import json

app=Flask(__name__)

@app.route('/msme',methods=['POST','GET'])
def home():
    if request.method=='POST':
             #data=request.args.get('q')#request.args['q']
             data = request.values.get('key')
             print(data)
             res='{'+'"Name":"{}"'.format(data)+'}'
             print (jsonify({"Name":"{}".format(data)}))
             return json.dumps(json.loads(res))
             
if __name__=='__main__':
	app.run()
