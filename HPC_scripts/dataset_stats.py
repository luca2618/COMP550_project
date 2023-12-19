import pickle


#with open('all_cleaned_reviews_female.pkl', 'rb') as f:
#    fr = pickle.load(f)
with open('all_cleaned_reviews_male.pkl', 'rb') as f:
    mr = pickle.load(f)

#print(len(fr))
print(len(mr))
