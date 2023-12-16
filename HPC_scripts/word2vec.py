from gensim.test.utils import common_texts
from gensim.models import Word2Vec
import numpy as np
import pandas as pd
import pickle

with open('all_cleaned_reviews_young.pkl', 'rb') as f:
    sentences = pickle.load(f)

print("nr of sentences:")
print(len(sentences))

#model 0 for CBOW, 1 for skipgram
#skipgram is used in Lucy2020 model
sg = 1

model = Word2Vec(sentences=sentences, vector_size=100, window=5, min_count=5, workers=4, sg=1)

word_vectors = model.wv
word_vectors.save("full_young.wordvectors")
