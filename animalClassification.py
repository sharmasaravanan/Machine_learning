import matplotlib.pyplot as plt
import numpy as np
import os
import cv2

import joblib
from skimage.io import imread
from skimage.transform import resize
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


def resize_all(src, width=150, height=150):
          
    data = dict()
    data['label'] = []
    data['data'] = []   

    for subdir in os.listdir(src):
        if subdir == ".DS_Store":
            continue
        current_path = os.path.join(src, subdir)
        for file in os.listdir(current_path):
            if file[-3:] in {'jpg', 'png'}:
                im = cv2.imread(os.path.join(current_path, file), 0)
                im = resize(im, (width, height))
                data['label'].append(subdir[:-4])
                data['data'].append(np.asarray(im).flatten())
    return data

data_path = '/Users/sharma/Downloads/Image'
os.listdir(data_path)

width = 80
 
data = resize_all(src=data_path)


from collections import Counter
 
print('number of samples: ', len(data['data']))
print('keys: ', list(data.keys()))
print('image shape: ', data['data'][0].shape)
print('labels:', np.unique(data['label']))
 
Counter(data['label'])

labels = np.unique(data['label'])
 
fig, axes = plt.subplots(1, len(labels))
fig.set_size_inches(200,200)
fig.tight_layout()

for ax, label in zip(axes, labels):
    idx = data['label'].index(label)
    im = cv2.resize(data['data'][idx], (500, 500))
    ax.imshow(im)
    ax.axis('off')
    ax.set_title(label)


X = np.array(data['data'])
y = np.array(data['label'])

X_train, X_test, y_train, y_test = train_test_split(
    X, 
    y, 
    test_size=0.2, 
    random_state=3,
)

model = RandomForestClassifier()

model.fit(X_train,y_train)

ypred = model.predict(X_test)

accuracy_score(ypred, y_test)