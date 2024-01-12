from gensim.models import KeyedVectors
import numpy as np
import pickle
import pandas as pd
from tqdm import tqdm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neural_network import MLPClassifier


with open('male.pkl', 'rb') as f:
    male_reviews = pickle.load(f)
with open('female.pkl', 'rb') as f:
    female_reviews = pickle.load(f)

def id(x):
    return x

tfidf = TfidfVectorizer(tokenizer=id, preprocessor=id, stop_words=None)

X = tfidf.fit_transform(male_reviews[:60000]+female_reviews[:60000])
Y = [1]*len(male_reviews[:60000])+[0]*len(female_reviews[:60000])
X_test = tfidf.transform(male_reviews[60000:80000]+female_reviews[60000:80000])
Y_test = [1]*len(male_reviews[60000:80000])+[0]*len(female_reviews[60000:80000])

# open a file, where you ant to store the data
file = open('tfidf.pkl', 'wb')

# dump information to that file
pickle.dump(tfidf, file)

# close the file
file.close()

model = MLPClassifier(random_state=1, max_iter=50,n_iter_no_change=3, early_stopping=True)
model.fit(X,Y)

# open a file, where you ant to store the data
file = open('important_model.pkl', 'wb')

# dump information to that file
pickle.dump(model, file)

# close the file
file.close()



print(">0.99")
results = []
for i, review in enumerate(X_test):
    #print(str(i), end='\r')
    guess = model.predict_proba(review)[0]
    if max(guess)>0.99:
        results.append(np.argmax(guess) == Y_test[i])
print("")
print(len(results))
print(np.mean(results))
print("Percentage of results")
print(len(results)/len(Y_test))

print(">0.95")
results = []
for i, review in enumerate(X_test):
    #print(str(i), end='\r')
    guess = model.predict_proba(review)[0]
    if max(guess)>0.95:
        results.append(np.argmax(guess) == Y_test[i])
print("")
print(len(results))
print(np.mean(results))
print("Percentage of results")
print(len(results)/len(Y_test))

print(">0.90")
results = []
for i, review in enumerate(X_test):
    #print(str(i), end='\r')
    guess = model.predict_proba(review)[0]
    if max(guess)>0.90:
        results.append(np.argmax(guess) == Y_test[i])
print("")
print(len(results))
print(np.mean(results))
print("Percentage of results")
print(len(results)/len(Y_test))