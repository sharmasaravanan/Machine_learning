import numpy as np
import scipy.misc
from keras.models import model_from_json
from keras.optimizers import Adam

#load model
model_architecture = 'cifar10_architecture.json'
model_weights = 'cifar10_weights.h5'
model = model_from_json(open(model_architecture).read())
model.load_weights(model_weights)

#load images
img_names = ['dog.jpeg', 'cat.jpg']
imgs = [np.transpose(scipy.misc.imresize(scipy.misc.imread(img_name), (28, 28)),(1, 0, 2)).astype('float32') for img_name in img_names]
imgs = np.array(imgs) / 255

'''
# train
optim = Adam()
model.compile(loss='categorical_crossentropy', optimizer=optim,metrics=['accuracy'])
'''

# predict
predictions = model.predict_classes(batch)
print(predictions)
