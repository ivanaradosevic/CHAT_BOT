from typing import List
import numpy as np
import pickle
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
from helpers import Intent, load_intents, get_lables

with open("tokenizer/tokenizer.pickle", "rb") as handle:
    tokenizer: Tokenizer = pickle.load(handle)

intents: List[Intent] = load_intents()
labels: List[str] = get_lables(intents)
model: Sequential = load_model("chatbot_model")
max_len: int = 20

def evaluate(input: str) -> str:
    sequences = tokenizer.texts_to_sequences([input])
    padded_sequences = pad_sequences(sequences, maxlen=max_len, truncating="post")
    result = model.predict(padded_sequences)
    prediction = np.argmax(result)
    tag = labels[prediction]
    
    for intent in intents:
        if tag == intent.tag:
            return np.random.choice(intent.responses)

    return "Didn't understand this. Please rephrase."