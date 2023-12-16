import pandas as pd
import csv
import string
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
#from tqdm import tqdm
import json
import pickle

lemmatizer = WordNetLemmatizer()

filename = "goodreads_reviews_young_adult.json"

sentences = []


with open(filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        try:
            dict_line = json.loads(line)
        except json.JSONDecodeError as e:
            # Print the error message
            print(f"JSONDecodeError: {e}")

            # Print the problematic character
            column_position = e.colno
            problematic_character = line[column_position - 1]
            print(f"Problematic character: {problematic_character}")
        # do something
        sentences.append(dict_line["review_text"])

translate_table = dict((ord(char), None) for char in string.punctuation) 
reviews = []

for review in sentences: #tqdm(sentences):
    if type(review) is str:
        review = review.lower().translate(translate_table)
        review = word_tokenize(review)
        review = [lemmatizer.lemmatize(word) for word in review]
        reviews.append(review)

with open('all_cleaned_reviews_young.pkl', 'wb') as f:
    pickle.dump(reviews, f)


    
