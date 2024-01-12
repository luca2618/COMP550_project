import pandas as pd
import csv
import string
#from tqdm import tqdm
import json
import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier

print("loading all reviews..")
with open('all_cleaned_reviews_young.pkl', 'rb') as f:
    reviews = pickle.load(f)
print("loading model..")
file = open('important_model.pkl', 'rb')

model = pickle.load(file)

# close the file
file.close()

def id(x):
    return x
print("loading tfid..")
with open('tfidf.pkl', 'rb') as f:
    tfidf = pickle.load(f)

male_reviews = []
female_reviews = []
print("Labelling:")
for i, review in enumerate(reviews):
    #print(str(i), end='\r')
    x = tfidf.transform([review])
    guess = model.predict_proba(x)[0]
    if max(guess)>0.95:
        if np.argmax(guess) == 1:
            male_reviews.append(review)
        if np.argmax(guess) == 0:
            female_reviews.append(review)
print("length of female")  
print(len(female_reviews))
print("length of male")
print(len(male_reviews))

with open('all_cleaned_reviews_female.pkl', 'wb') as file:
    pickle.dump(female_reviews, file)
with open('all_cleaned_reviews_male.pkl', 'wb') as file2:
    pickle.dump(male_reviews, file2)