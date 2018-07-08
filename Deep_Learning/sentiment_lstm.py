from keras.layers.core import Activation, Dense, Dropout
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import LSTM
from keras.models import Sequential
from keras.preprocessing import sequence
from sklearn.model_selection import train_test_split
import collections
import matplotlib.pyplot as plt
import nltk
import numpy as np
import os

maxlen = 0
word_freqs = collections.Counter()
num_recs = 0

ftrain = open("./training.txt", "r")

for line in ftrain:
	label, sentence = line.strip().split("\t")
	words = nltk.word_tokenize(sentence.lower())
	if len(words) > maxlen:
		maxlen = len(words)
	for word in words:
		word_freqs[word] += 1
	num_recs += 1
ftrain.close()

#print(maxlen)
#print(len(word_freqs))

MAX_FEATURES = 2000
MAX_SENTENCE_LENGTH = 40
'''
for i, x in enumerate(word_freqs.most_common(MAX_FEATURES)):
	print(i,x)
'''
vocab_size = min(MAX_FEATURES, len(word_freqs)) + 2
word2index = {x[0]: i+2 for i, x in enumerate(word_freqs.most_common(MAX_FEATURES))}
word2index["PAD"] = 0
word2index["UNK"] = 1
index2word = {v:k for k, v in word2index.items()}

X = np.empty((num_recs, ), dtype=list)
y = np.zeros((num_recs, ))
i = 0

ftrain = open("./training.txt", "r")

for line in ftrain:
	label, sentence = line.strip().split("\t")
	words = nltk.word_tokenize(sentence.lower())
	seqs = []
	for word in words:
		if word in word2index:
			seqs.append(word2index[word])
		else:
			seqs.append(word2index["UNK"])
	X[i] = seqs
	y[i] = int(label)
	i += 1
ftrain.close()

X = sequence.pad_sequences(X, maxlen=MAX_SENTENCE_LENGTH)

#print(X)

Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=42)

EMBEDDING_SIZE = 128
HIDDEN_LAYER_SIZE = 64
BATCH_SIZE = 32
NUM_EPOCHS = 10

model = Sequential()
model.add(Embedding(vocab_size, EMBEDDING_SIZE,input_length=MAX_SENTENCE_LENGTH))
model.add(Dropout(0.2))
model.add(LSTM(HIDDEN_LAYER_SIZE, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(1))
model.add(Activation("sigmoid"))
model.compile(loss="binary_crossentropy", optimizer="adam",metrics=["accuracy"])
model.summary()

history = model.fit(Xtrain, ytrain, batch_size=BATCH_SIZE, epochs=NUM_EPOCHS,validation_data=(Xtest, ytest))

score, acc = model.evaluate(Xtest, ytest, batch_size=BATCH_SIZE)
print("Test score: %.3f, accuracy: %.3f" % (score, acc))

plt.subplot(211)
plt.title("Accuracy")
plt.plot(history.history["acc"], color="g", label="Train")
plt.plot(history.history["val_acc"], color="b", label="Validation")
plt.legend(loc="best")
plt.subplot(212)
plt.title("Loss")
plt.plot(history.history["loss"], color="g", label="Train")
plt.plot(history.history["val_loss"], color="b", label="Validation")
plt.legend(loc="best")
plt.tight_layout()
plt.show()

for i in range(5):
	idx = np.random.randint(len(Xtest))
	xtest = Xtest[idx].reshape(1,40)
	ylabel = ytest[idx]
	ypred = model.predict(xtest)[0][0]
	sent = " ".join([index2word[x] for x in xtest[0].tolist() if x != 0])
	print("%.0f\t%d\t%s" % (ypred, ylabel, sent))

text ="Before I left Missouri, I thought London was going to be so good and cool and fun and a really great experience and I was really excited."

words = nltk.word_tokenize(text.lower())
seqs_test = []
for word in words:
	if word in word2index:
		seqs_test.append(word2index[word])
	else:
		seqs_test.append(word2index["UNK"])

seqs_test = sequence.pad_sequences([seqs_test], maxlen=MAX_SENTENCE_LENGTH)
test = seqs_test.reshape(1,40)

print("Real Time :",model.predict_classes(test)[0][0])

