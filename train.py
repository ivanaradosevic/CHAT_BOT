from typing import List
import numpy as np
import pickle
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, GlobalAveragePooling1D, Embedding
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from helpers import Intent, load_intents

intents: List[Intent] = load_intents()

training_sentences: List[str] = []
training_labels: List[str] = []
labels: List[str] = []

responses: List[str] = []

for intent in intents:
    for pattern in intent.patterns:
        training_sentences.append(pattern)
        training_labels.append(intent.tag)

    responses.append(intent.responses)

    if intent.tag not in labels:
        labels.append(intent.tag)

vectorized_training_labels = [labels.index(tag) for tag in training_labels]

vocab_size = 1000
max_len = 20
embedding_dim = 16
oov_token = "<OOV>"
num_classes = len(labels)
epochs = 500

tokenizer = Tokenizer(vocab_size, oov_token=oov_token)
tokenizer.fit_on_texts(training_sentences)
sequences = tokenizer.texts_to_sequences(training_sentences)
padded_sequences = pad_sequences(sequences, maxlen=max_len, truncating="post")

model = Sequential()
model.add(Embedding(vocab_size, embedding_dim, input_length=max_len))
model.add(GlobalAveragePooling1D())
model.add(Dense(64, activation="relu"))
model.add(Dense(64, activation="relu"))
model.add(Dense(num_classes, activation="softmax"))
model.compile("adam", "sparse_categorical_crossentropy", ["accuracy"])

model.summary()

model.fit(padded_sequences, np.array(vectorized_training_labels), epochs=epochs)
model.save("chatbot_model")

with open("tokenizer/tokenizer.pickle", "wb") as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

