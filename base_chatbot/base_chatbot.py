import numpy as np
import pandas as pd
import json
import string
import random

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Input, Embedding, LSTM, GlobalMaxPooling1D, Flatten, Dense
from keras.models import Model
from sklearn.preprocessing import LabelEncoder

from details.movie_indication import Indications
from details.cast_details import CastDetails
from details.crew_details import CrewDetails
from details.movie_details import MovieDetails



#import the dataset base_chatbot/content.json
with open('base_chatbot/content.json') as content:
    data1 = json.load(content)

#getting all the data to lists
tags = []
inputs = []
responses = {}
for intent in data1['intents']:
    responses[intent['tag']] = intent['responses']
    for lines in intent['input']:
        inputs.append(lines)
        tags.append(intent['tag'])

    
#converting dataframe
data = pd.DataFrame({"inputs":inputs,"tags":tags})
#print(data)

data['inputs'] = data['inputs'].apply(lambda wrd:[ltrs.lower() for ltrs in wrd if ltrs not in string.punctuation])

data['inputs'] = data['inputs'].apply(lambda wrd: ''.join(wrd))


#tokenize data
tokenizer = Tokenizer(num_words=6000)
tokenizer.fit_on_texts(data['inputs'])
train = tokenizer.texts_to_sequences(data['inputs'])


#apllying padding
x_train = pad_sequences(train)

#enconding outputs
le = LabelEncoder()
y_train = le.fit_transform(data['tags'])
#print(y_train)

#input length
input_shape = x_train.shape[1]
#print(input_shape)

#define vocabulary
vocabulary = len(tokenizer.word_index)


#output_length
output_length = le.classes_.shape[0]


#creating model
i = Input(shape=(input_shape,))
x = Embedding(vocabulary+1, 20)(i)
x = LSTM(10, return_sequences=True)(x)
x = Flatten()(x)
x = Dense(output_length, activation="softmax")(x)
model = Model(i, x)


#commpiling the model
model.compile(loss="sparse_categorical_crossentropy", optimizer='adam', metrics=['accuracy'])

#training the model
train = model.fit(x_train, y_train, epochs=500)


#chatting
while True:
    text_p = []
    prediction_input = input('You : ')

    #removing punctuation and converting to lowercase
    prediction_input = [letters.lower() for letters in prediction_input if letters not in string.punctuation]
    prediction_input = ''.join(prediction_input)
    
    text_p.append(prediction_input)
    
    #tokenizing and padding
    prediction_input = tokenizer.texts_to_sequences(text_p)
    prediction_input = np.array(prediction_input).reshape(-1)
    prediction_input = pad_sequences([prediction_input], input_shape)
    
    #getting output from model
    output = model.predict(prediction_input)
    output = output.argmax()
    
    #finding the right tag and predicting
    response_tag = le.inverse_transform([output])[0]
    print("CineBot : ", random.choice(responses[response_tag]))
    if response_tag == "searchfilm":
        #from details.movie_indication import Indications
        try:
            Indications().detailed_match()
        except:
            print("Me desculpe! Ocorreu um problema, para mais informações digite a opção: Erros")
        
    
    if response_tag == "searchcast":
        
        try:
            CastDetails().detailed_matches()
        except:
            print("Me desculpe! Ocorreu um problema, para mais informações digite a opção: Erros")
    
    if response_tag == "searchcrew":
        #from details.crew_details import CrewDetails
        try:
            CrewDetails().detailed_matches()
        except:
            print("Me desculpe! Ocorreu um problema, para mais informações digite a opção: Erros")

    if response_tag == "detailMovie":
        try:
            print(MovieDetails().movie_details())
        except:
            print("Me desculpe! Ocorreu um problema, para mais informações digite a opção: Erros")

    if response_tag == "goodbye":
        break