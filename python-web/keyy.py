from flask import Flask,request
import json

app=Flask(__name__)

@app.route('/ai',methods=['POST','GET'])
def preprocess():
    if request.method=='POST':
             #data=request.args.get('q')
             data = request.values.get('keying')
             print(data)
             res='{'+'"Name":"{}"'.format(data)+'}'
             return json.dumps(json.loads(res))
             
if __name__=='__main__':
	app.run(host='0.0.0.0',port=8080)
