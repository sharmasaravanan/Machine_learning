import streamlit as st
import time
import pickle
import re

from bs4 import BeautifulSoup
from flask import Flask, render_template, request
import nltk
nltk.download('stopwords') 
from nltk.corpus import stopwords

st.set_page_config(page_title='Movie Review Sentiment Analysis')
st.write("""## Movie Review Sentiment Analysis
Using ML Algorithm!""")

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


txt = st.text_area('Review to analyze', placeholder="Please enter any movie review.")
if st.button('Analyze'):
    with st.spinner('Wait for it...'):
        time.sleep(5)
    result = model.predict(vect.transform([cleaning(txt)]))[0]
    score = max(model.predict_proba(vect.transform([cleaning(txt)]))[0]) * 100
    if result == 0:
        sentiment = "Negative"
    else:
        sentiment = "Positive"
    st.markdown("---")
    st.write("Sentiment is {} with the score {:.2f}%".format(sentiment, score))
    st.markdown("---")
