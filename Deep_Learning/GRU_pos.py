import collections
import nltk

import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.python.keras.layers import Dense, GRU, Embedding
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.optimizers import Adam
from tensorflow.python.keras.preprocessing.sequence import pad_sequences

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

#for i, x in enumerate(word_freqs.most_common(MAX_FEATURES)):
#	print(i,x)

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

X = pad_sequences(X, maxlen=MAX_SENTENCE_LENGTH)

Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=42)


embedding_size = 8
optimizer = Adam(lr=1e-4)


model = Sequential()
model.add(Embedding(input_dim=4000, output_dim=128, input_length=40,name='layer_embedding'))
model.add(GRU(units=16, name = "gru_1",return_sequences=True))
model.add(GRU(units=8, name = "gru_2" ,return_sequences=True))
model.add(GRU(units=4, name= "gru_3"))
model.add(Dense(1, activation='sigmoid',name="dense_1"))
model.compile(loss='binary_crossentropy',optimizer=optimizer,metrics=['accuracy'])
model.summary()

history = model.fit(Xtrain, ytrain,validation_split=0.05, epochs=20, batch_size=32)


score, acc = model.evaluate(Xtest, ytest, batch_size=32)
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
	print("Predicted\tActual\t\tsentence")
	print("%.0f\t\t%d\t%s" % (ypred, ylabel, sent))

text = "Now I can totally rub it in my dad's face that Seattle sucks more than Pittsburgh does."

words = nltk.word_tokenize(text.lower())
seqs_test = []

for word in words:
	if word in word2index:
		seqs_test.append(word2index[word])
	else:
		seqs_test.append(word2index["UNK"])
		
seqs_test = 	pad_sequences([seqs_test], maxlen=MAX_SENTENCE_LENGTH)
test = seqs_test.reshape(1,40)

print("Real Time :",model.predict_classes(test)[0][0])

