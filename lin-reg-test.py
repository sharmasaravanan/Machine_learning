import pickle

fname="model.sav"

loaded=pickle.load(open(fname, 'rb'))

y_pred = loaded.predict([[200,16.5,36]])

#print(np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

print y_pred
