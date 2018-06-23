from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import pandas as pd

data=pd.read_csv("./weather.csv")

print (data.head())

features=["outlook","temperature","humidity","wind"]

x=data[features]

y=data.play

nb_model = GaussianNB()

nb_model.fit(x, y)

preds = nb_model.predict([[2,1,1,1]])

#preds = model.predict([[2,0,1,1]])


print (preds)
