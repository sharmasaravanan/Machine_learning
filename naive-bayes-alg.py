from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import pandas as pd

data=pd.read_csv("./weather.csv")

print data.head()

features=["outlook","temperature","humidity","wind"]

x=data[features]

y=data.play

nb_model = GaussianNB()

model = nb_model.fit(x, y)

preds = gnb.predict([sunny,cool,high,True])
