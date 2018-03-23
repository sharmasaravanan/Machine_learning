from sklearn import tree

model=tree.DecisionTreeClassifier()

x=[[180,15,0],[167,42,1],[136,35,1],[174,15,0],[141,28,1]]

y=['man','woman','woman','man','woman']

model=model.fit(x,y)

prediction=model.predict([[133,37,1]])

print prediction
