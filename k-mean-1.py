import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans

data = pd.read_csv("./Advertising.csv", index_col=0)

feature_names = ['TV', 'radio', 'newspaper']

X = data[feature_names]

kmeans = KMeans().fit(X)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_

print(centroids)
print(labels)

colors = ["g.","r.","c.","y."]

#plt.scatter(centroids[:, 0],centroids[:, 1], centroids[:, 2],marker = "x", linewidths = 5, zorder = 10)

#plt.show()
