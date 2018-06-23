import pandas as pd

from sklearn.ensemble import RandomForestClassifier

train = pd.read_csv("train.csv")

test = pd.read_csv("test.csv")

cols = ['petal_length', 'petal_width', 'sepal_length', 'sepal_width'] 

colsRes = ['class']

trainArr = train.as_matrix(cols) 

trainRes = train.as_matrix(colsRes)

rf = RandomForestClassifier(n_estimators=100) 

rf.fit(trainArr, trainRes)

testArr = test.as_matrix(cols)

results = rf.predict(testArr)

test['predictions'] = results

test.head()

