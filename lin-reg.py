import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# import pickle


data = pd.read_csv("./Advertising.csv", index_col=0)

feature_names = ['TV', 'radio', 'newspaper']

X = data[feature_names]

y = data.sales

X_train, X_test, y_train, y_test = train_test_split(X, y)

linreg = LinearRegression()

linreg.fit(X_train, y_train)

#fname="model.sav"

#pickle.dump(linreg, open(fname, 'wb'))

y_pred = linreg.predict(X_test)

print(np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
