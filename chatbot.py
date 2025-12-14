import random
import numpy as np
import pickle
import json
import nltk
from nltk.stem import WordNetLemmatizer
from keras.models import load_model

lenmatizer = WordNetLemmatizer()
intents = json.loads(open('intents_spanish.json', 'r', encoding='utf-8').read())

words = pickle.load(open('words_spanish.pkl', 'rb'))
classes = pickle.load(open('classes_spanish.pkl', 'rb'))
model = load_model('chatbot_model_spanish.h5')

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence, language='spanish')
    sentence_words = [lenmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def get_response(ints, intents_json):
    tag = ints[0]['intent']
    for intent in intents_json['intents']:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])
