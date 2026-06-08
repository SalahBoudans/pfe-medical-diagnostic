import random
import json
import pickle
import numpy as np
import nltk
import tensorflow as tf
from .nltk_utils import bag_of_words, tokenize, stem
from keras.models import load_model

# Load the JSON file into a Python dictionary
with open('App1/data.json', 'r', encoding='utf-8') as file:
    intents = json.load(file)

all_words = pickle.load(open('all_words.pkl', 'rb'))
classes = pickle.load(open('tags.pkl', 'rb'))
model = load_model('chatbot__model.h5')

def traitment(sentence):
    
    sentence = tokenize(sentence)
    ignore_words = ['?', '.', '!',',',':',';']
    list_sentence  = [stem(w) for w in sentence if w not in ignore_words]
    final_sentence = bag_of_words(list_sentence, all_words)
    
    return final_sentence

def predict_class (sentence):
    sentence = traitment(sentence)
    print(len(sentence))
    res = model.predict(np.array([sentence]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes [r[0]], 'probability': str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice (i['responses'])
            break
    return result

# while True:
#     message = input("")
#     if message == 'exit':
#         break
#     ints = predict_class (message)
#     res = get_response (ints, intents)
#     print (res)

