import pickle
import re

from bs4 import BeautifulSoup
from flask import Flask, render_template, request
from nltk.corpus import stopwords

app = Flask(__name__)
vect = pickle.load(open("./vector.pickel", "rb"))
model = pickle.load(open("./LogisticRegressionModel.pickel", "rb"))
stop = stopwords.words('english')


def cleaning(raw):
    exam = BeautifulSoup(raw, "html.parser")
    letters = re.sub("[^a-zA-Z]", " ", exam.get_text())
    low = letters.lower()
    words = low.split()
    useful = [w for w in words if w not in stop]
    return " ".join(useful)


@app.route('/', methods=['POST', 'GET'])
def hello():
    if request.method == 'GET':
        return render_template('testing.html')
    elif request.method == 'POST':
        na = request.form['img']
        result = model.predict(vect.transform([cleaning(na)]))[0]
        score = max(model.predict_proba(vect.transform([cleaning(na)]))[0])
        if result == 0:
            sentiment = "Negative"
        else:
            sentiment = "Positive"
        kwargs = {'name': "Sentiment is {} with the score {:.2f}".format(sentiment, score)}
        return render_template("testing.html", **kwargs)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8005)
