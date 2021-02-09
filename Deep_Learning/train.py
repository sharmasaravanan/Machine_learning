from tensorflow.keras.datasets import cifar10
from tensorflow.keras.layers import Dense, Dropout, Flatten, BatchNormalization, Activation
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.models import Sequential
from tensorflow.keras.utils import to_categorical

#constant
epochs = 25  
optimizer = 'adam'  

# loading in the data
# CIFAR_10 is a set of 60K images 32x32 pixels on 3 channels
(X_train, y_train), (X_test, y_test) = cifar10.load_data()

print('X_train shape:', X_train.shape)
print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')

# one hot encode outputs
y_train = to_categorical(y_train)  
y_test = to_categorical(y_test)  
class_num = y_test.shape[1]

# normalize the inputs from 0-255 to between 0 and 1 by dividing by 255

X_train = X_train.astype('float32')  
X_test = X_test.astype('float32')  
X_train = X_train / 255.0  
X_test = X_test / 255.0  

# network
model = Sequential()
model.add(Conv2D(20, kernel_size=5, input_shape=X_train.shape[1:], padding='same'))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

model.add(Conv2D(50, kernel_size=5, padding='same'))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))

model.add(Flatten())
model.add(Dense(500))
model.add(Activation("relu"))
model.add(Dense(10))
model.add(Activation("softmax"))
model.summary()

# train
model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])  
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=epochs, batch_size=64)  


# Model evaluation
scores = model.evaluate(X_test, y_test, verbose=0)  
print("Accuracy: %.2f%%" % (scores[1]*100))


