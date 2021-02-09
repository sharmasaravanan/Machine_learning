import MySQLdb
from flask import Flask, render_template, url_for, redirect, request

db = MySQLdb.connect(host="localhost", user="admin", passwd="test@123", db="testDB")

cur = db.cursor()

app=Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def hello():
    if request.method == 'GET':
        return render_template('testing.html')
    elif request.method == 'POST':
        na = request.form['img']
        cur.execute("SELECT Passport_Number FROM testDB.PassportDetails where Person_Id = {}".format(na))
        kwargs = {'name': cur.fetchone()[0], }
        return render_template("testing.html", **kwargs)

@app.route('/testing',methods=['GET'])
def test():
	if request.method=='GET':
		return render_template("hello.html")
		
@app.route('/play')
def playing():
    # return redirect(url_for('test'))
    return redirect('testing')
	
if __name__=='__main__':
    app.run(host="0.0.0.0", port=8005)
