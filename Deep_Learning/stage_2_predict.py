import numpy as np
import scipy.misc
import cv2
from keras.models import model_from_json
from keras.optimizers import SGD

#load model
model_architecture = 'CNN_architecture.json'
model_weights = 'CNN_weights.h5'
model = model_from_json(open(model_architecture).read())
model.load_weights(model_weights)
'''
#load images
img_names = ['zeros.png', 'second.png']
imgs = [np.transpose(scipy.misc.imresize(scipy.misc.imread(img_name), (28, 28)),(1, 0, 2)).astype('float32') for img_name in img_names]
imgs = np.array(imgs) / 255
'''
img = cv2.imread('zeros.png')
img = cv2.resize(img,(28,28))
img = img.astype("float") / 255.0
#img = np.reshape(img,[28,28,1])
#img=img.flatten().reshape(1, 784)
batch = np.expand_dims(img,axis=0)
print(batch.shape) # (1, 28, 28)
batch = np.expand_dims(batch,axis=3)
print(batch.shape) # (1, 28, 28,1)

# predict
predictions = model.predict_classes(batch)
print(predictions)
