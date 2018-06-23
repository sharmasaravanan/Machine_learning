import pickle

fname="model.sav"

loaded=pickle.load(open(fname, 'rb'))

y_pred = loaded.predict([[200,16.5,78]])

print y_pred
