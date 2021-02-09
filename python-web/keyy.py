from flask import Flask, request, jsonify

app=Flask(__name__)

@app.route('/python',methods=['POST','GET'])
def home():
    if request.method=='GET':
        data = request.args.get('q')  # request.args['q']
        # data = request.values.get('fruit')
        print(data)
        res = {}
        res["Name"] = data
        res["Class"] = "Python"
        return jsonify(res)

             
if __name__=='__main__':
    app.run()
