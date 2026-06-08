import numpy as np
import json
import tensorflow as tf
import pickle

from nltk_utils import bag_of_words, tokenize, stem

with open('App1/data.json', 'r') as f:
    intents = json.load(f)

all_words = []
tags = []
xy = []
# loop through each sentence in our intents patterns
for intent in intents['intents']:
    tag = intent['tag']
    # add to tag list
    tags.append(tag)
    for pattern in intent['patterns']:
        # tokenize each word in the sentence
        w = tokenize(pattern)
        # add to our words list
        all_words.extend(w)
        # add to xy pair
        xy.append((w, tag))
# stem and lower each word
ignore_words = ['?', '.', '!',',',':',';']
all_words = [stem(w) for w in all_words if w not in ignore_words]
# remove duplicates and sort
all_words = sorted(set(all_words))
tags = sorted(set(tags))

pickle.dump(all_words, open('all_words.pkl', 'wb'))
pickle.dump(tags, open('tags.pkl', 'wb'))

# all_words = pickle.load(open('words.pkl', 'rb'))
# create training data
X_train = []
y_train = []
outputEmpty = np.zeros(len(tags))
for (pattern_sentence, tag) in xy:
    # X: bag of words for each pattern_sentence
    bag = bag_of_words(pattern_sentence, all_words)
    X_train.append(bag)
    # y: PyTorch CrossEntropyLoss needs only class labels, not one-hot
    label = tags.index(tag)
    outputRow = list(outputEmpty)
    outputRow[tags.index(tag)] = 1
    y_train.append(outputRow)

X_train = np.array((X_train))
y_train = np.array(y_train)
model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(128, input_shape=(len(X_train[0]),), activation = 'relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(64, activation = 'relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(len(y_train[0]), activation='softmax'))

sgd = tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

hist = model.fit(X_train,y_train, epochs=200, batch_size=5, verbose=1)

model.save('chatbot_model__.h5', hist)
print('Done')
