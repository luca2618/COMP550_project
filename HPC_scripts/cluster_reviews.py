from gensim.models import KeyedVectors
import matplotlib.pyplot as plt
from semaxis import *
import numpy as np
import pickle
import pandas as pd
from tqdm import tqdm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold

with open('./datasets/male.pkl', 'rb') as f:
    male_reviews = pickle.load(f)
with open('./datasets/female.pkl', 'rb') as f:
    female_reviews = pickle.load(f)


tfidf = TfidfVectorizer(tokenizer=lambda x: x,
                        preprocessor=lambda x: x, stop_words=None)
X = tfidf.fit_transform(male_reviews+female_reviews)
Y = [1]*len(male_reviews)+[0]*len(female_reviews)


kf = KFold(n_splits=5, random_state=None, shuffle=False)
results = []
for k, (train_index, test_index) in enumerate(kf.split(X)):
    X_train = X[train_index]
    y_train = [Y[idx] for idx in train_index]
    X_test = X[test_index]
    y_test = [Y[idx] for idx in test_index]
    print(f"Fold {k}:")
    fold_results = []
    model = MLPClassifier(random_state=1, max_iter=300)
    model.fit(X_train,y_train)
    for i, review in enumerate(X_test):
        #print(str(i), end='\r')
        guess = model.predict_proba(review)[0]
        if max(guess)>0.7:
            fold_results.append(np.argmax(guess) == y_test[i])
    results.append(np.mean(fold_results))
print(results)
results = np.array(results)
print("%0.2f accuracy with a standard deviation of %0.2f" % (results.mean(), results.std()))

