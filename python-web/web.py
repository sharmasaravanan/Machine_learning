
from flask import Flask,render_template,url_for,redirect,request

app=Flask(__name__)

@app.route('/home', methods=['POST', 'GET'])
def hello():
    if request.method == 'GET':
                return render_template('testing.html')
    elif request.method == 'POST':
    		na=request.form['img']
    		kwargs={'name':na,}
    		return render_template("testing.html",**kwargs)

@app.route('/testing',methods=['GET'])
def test():
	if request.method=='GET':
		return render_template("hello.html")
		
@app.route('/play')
def playing():
	return redirect(url_for('test'))
	
if __name__=='__main__':
    app.run(host="127.10.10.10")
