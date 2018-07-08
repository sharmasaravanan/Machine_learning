from keras.layers import Dense, Activation
from keras.layers.recurrent import SimpleRNN
from keras.models import Sequential
#from keras.utils.visualize_util import plot
import numpy as np

fin = open("11.txt", 'rb')
lines = []
for line in fin:
	line = line.strip().lower()
	line = line.decode("ascii", "ignore")
	if len(line) == 0:
		continue
	lines.append(line)
fin.close()

text = " ".join(lines)

chars = set([c for c in text])
nb_chars = len(chars)

char2index = dict((c, i) for i, c in enumerate(chars))
index2char = dict((i, c) for i, c in enumerate(chars))

SEQLEN = 10
STEP = 1
input_chars = []
label_chars = []
for i in range(0, len(text) - SEQLEN, STEP):
	input_chars.append(text[i:i + SEQLEN])
	label_chars.append(text[i + SEQLEN])

X = np.zeros((len(input_chars), SEQLEN, nb_chars), dtype=np.bool)#5000 x 10 x 55
y = np.zeros((len(input_chars), nb_chars), dtype=np.bool)

for i, input_char in enumerate(input_chars):
	for j, ch in enumerate(input_char):
		X[i, j, char2index[ch]] = 1
		y[i, char2index[label_chars[i]]] = 1

HIDDEN_SIZE = 128
BATCH_SIZE = 128
NUM_ITERATIONS = 25
NUM_EPOCHS_PER_ITERATION = 1
NUM_PREDS_PER_EPOCH = 100

model = Sequential()
model.add(SimpleRNN(HIDDEN_SIZE, return_sequences=False,input_shape=(SEQLEN, nb_chars),unroll=True))
model.add(Dense(nb_chars))
model.add(Activation("softmax"))
model.compile(loss="categorical_crossentropy", optimizer="rmsprop")
model.summary()

for iteration in range(NUM_ITERATIONS):
	print("=" * 50)
	print("Iteration #: %d" % (iteration))
	model.fit(X, y, batch_size=BATCH_SIZE, epochs=NUM_EPOCHS_PER_ITERATION)
	#test_idx = np.random.randint(len(input_chars))
	test_chars = "are and hi"
	print("Generating from seed: %s" % (test_chars))
	print(test_chars, end="")
	for i in range(NUM_PREDS_PER_EPOCH):
		Xtest = np.zeros((1, SEQLEN, nb_chars))
		for i, ch in enumerate(test_chars):
			Xtest[0, i, char2index[ch]] = 1
		pred = model.predict(Xtest, verbose=0)[0]
		ypred = index2char[np.argmax(pred)]
		print(ypred, end="")
		# move forward with test_chars + ypred
		test_chars = test_chars[1:] + ypred
print()

