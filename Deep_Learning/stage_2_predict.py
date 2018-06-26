import numpy as np
import scipy.misc
from keras.models import model_from_json
from keras.optimizers import SGD

#load model
model_architecture = 'CNN_architecture.json'
model_weights = 'CNN_weights.h5'
model = model_from_json(open(model_architecture).read())
model.load_weights(model_weights)

#load images
img_names = ['cat-standing.jpg', 'dog.jpg']
imgs = [np.transpose(scipy.misc.imresize(scipy.misc.imread(img_name), (32, 32)),(1, 0, 2)).astype('float32') for img_name in img_names]
imgs = np.array(imgs) / 255

# predict
predictions = model.predict_classes(imgs)
print(predictions)
