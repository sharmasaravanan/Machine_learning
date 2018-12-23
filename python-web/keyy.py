from flask import Flask, request, jsonify

app=Flask(__name__)

@app.route('/python',methods=['POST','GET'])
def home():
    if request.method=='POST':
        data = request.args.get('q')  # request.args['q']
        # data = request.values.get('fruit')
             print(data)
        res = {}
        res["Name"] = data
        return jsonify(res)
        #return json.dumps(res)
             
if __name__=='__main__':
	app.run(host="0.0.0.0",port=8000)
