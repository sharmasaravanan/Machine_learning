import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
import pickle


data = pd.read_csv("./Advertising.csv", index_col=0)

feature_names = ['TV', 'radio', 'newspaper']

X = data[feature_names]

y = data.sales

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

linreg = LinearRegression()

linreg.fit(X_train, y_train)

fname="model.sav"

pickle.dump(linreg, open(fname, 'wb'))


#y_pred = linreg.predict(X_test)

#print(np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
