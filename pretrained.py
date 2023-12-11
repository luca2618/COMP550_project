from gensim.models import KeyedVectors
import matplotlib.pyplot as plt
from semaxis import *

# Path to the pretrained Word2Vec model file
pretrained_model_path = './datasets/GoogleNews-vectors-negative300.bin'

# Load the Word2Vec model
word2vec_model = KeyedVectors.load_word2vec_format(pretrained_model_path, binary=True)

# Example usage
word_embedding = word2vec_model['cake']
print(f'Embedding for "cake": {word_embedding}')

# Find similar words
similar_words = word2vec_model.most_similar('cake', topn=5)
print(f'Similar words to "cake": {similar_words}')