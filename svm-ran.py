import numpy as np
from sklearn import svm

x =np.array([[1,2],
             [5,8],
             [1.5,1.8],
             [8,8],
             [1,0.6],
             [9,11]])
y = [0,1,0,1,0,1]

clf = svm.SVC(kernel='linear', probability=True)
clf.fit(x,y)

clf.predict([[0.58, 0.76]])

clf.predict([[10.58, 10.76]])
