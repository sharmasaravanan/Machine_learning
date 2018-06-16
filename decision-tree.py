from sklearn import tree

import pandas as pd

df=pd.read_csv("./weather.csv")

model=tree.DecisionTreeClassifier()

x = df.loc[:,"outlook":"wind"]

y = df.play

model = model.fit(x,y)

prediction=model.predict([[2,1,1,1]])

print prediction
