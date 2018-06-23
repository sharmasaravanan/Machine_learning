from flask import Flask,render_template
import sys,os

app = Flask(__name__)

@app.route('/hello')
def home():
    a="hello sharma"
    return a

if __name__ == '__main__':
    app.debug = True
    app.run()
