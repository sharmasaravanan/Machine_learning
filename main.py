import matplotlib

matplotlib.use("TKAgg")

import matplotlib.pyplot as plt
from tensorflow.keras.layers import *
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.optimizers import Adam

import numpy as np
import os
import pickle

# dataset directory
data_path = '/Users/sharma/Downloads/Image'
os.listdir(data_path)

labelCode  = {'Tiger': 0,
 'Dog': 1,
 'Rabbit': 2,
 'Pig': 3,
 'Lion': 4,
 'Bear': 5,
 'Elephant': 6,
 'Mouse': 7,
 'Eagle': 8,
 'Human': 9,
 'Duck': 10,
 'Chicken': 11,
 'Monkey': 12,
 'Cow': 13,
 'Wolf': 14,
 'Sheep': 15,
 'Pigeon': 16,
 'Panda': 17,
 'Cat': 18,
 'Deer': 19}

codeLabel = dict((v,k)for k,v in labelCode.items())

def resize_all(src, width=150, height=150):
          
    data = dict()
    data['label'] = []
    data['data'] = []   
    temp = {}

    for subdir in os.listdir(src):
        if subdir == ".DS_Store":
            continue
        current_path = os.path.join(src, subdir)
        for file in os.listdir(current_path):
            if file[-3:] in {'jpg', 'png'}:
                im = cv2.imread(os.path.join(current_path, file), 0)
                im = resize(im, (width, height))
                label = subdir[:-4]

                if label in temp:
                    temp[label] += 1
                else:
                    temp[label] = 1
                
                if temp[label] <100:
                    data['label'].append(labelCode[label])
                    data['data'].append(np.asarray(im).flatten())
    return data

data = resize_all(src=data_path)

X = np.array(data['data'])
y = np.array(data['label'])

<split it>

# converting into array
x_train = np.array(x_train)
x_test = np.array(x_test)
y_train = np.array(y_train)
y_test = np.array(y_test)

print("Shapes of the train and test dataset are {} and {}".format(x_train.shape, x_test.shape))

outputClasses = len(set(y_train))
print("Total number of classes are {}".format(outputClasses))

# encoding to labels to binary data
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

# float conversion and normalising dataset
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

# creating a neural network model
model = Sequential()
model.add(Conv2D(32, (3, 3), input_shape=x_train.shape[1:], activation='relu', padding='same'))
model.add(Dropout(0.1))
model.add(BatchNormalization())

model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.1))
model.add(BatchNormalization())

model.add(Conv2D(128, (3, 3), activation='relu', padding='same'))
model.add(Dropout(0.1))
model.add(BatchNormalization())

model.add(Flatten())
model.add(Dropout(0.1))

model.add(Dense(256))
model.add(Activation('relu'))
model.add(Dropout(0.1))
model.add(BatchNormalization())

model.add(Dense(128))
model.add(Activation('relu'))
model.add(Dropout(0.1))
model.add(BatchNormalization())

model.add(Dense(outputClasses))
model.add(Activation('softmax'))

# compling the neural network
model.compile(loss='categorical_crossentropy', optimizer=Adam(), metrics=['accuracy'])

# summary of the model
model.summary()

# training the model with train dataset
history = model.fit(x_train, y_train, validation_split=0.1, epochs=30, batch_size=64)

# plotting the training and validation values
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('Training and Validation accuracy')
plt.ylabel('accuracy')
plt.xlabel('epochs')
plt.legend(['train', 'validation'])
plt.show()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Training and Validation loss')
plt.ylabel('loss')
plt.xlabel('epochs')
plt.legend(['train', 'validation'])
plt.show()

# cross validating with the test data
result = model.evaluate(x_test, y_test, verbose=0)
print("Accuracy: {:.2f}%".format(result[1] * 100))

im = cv2.imread("/Users/sharma/Downloads/tiger.png", 0)
im = resize(im, (150, 150))

model.predict([[np.array(im).flatten()]])

codeLabel[model.predict_classes([[np.array(im).flatten()]])[0]]