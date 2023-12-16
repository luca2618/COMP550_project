# basic libraries
import pandas as pd
import json
import pickle

def load_df_from_json(filename):
  with open(filename, 'r') as f:
    json_dict = json.load(f)
    df = pd.read_json(json_dict)
  return df


preprocessed_df = load_df_from_json('./HPC_scripts/preprocessed_reviews_dataset.json')

male = []
female = []
mixed = []

for ind in preprocessed_df.index:
    print(ind)
    if preprocessed_df['PROTAGONIST'][ind] == 'F':
       female.append(preprocessed_df['PREPROCESSED_REVIEW'][ind])
    elif preprocessed_df['PROTAGONIST'][ind] == 'M':
       male.append(preprocessed_df['PREPROCESSED_REVIEW'][ind])
    elif preprocessed_df['PROTAGONIST'][ind] == 'V':
       mixed.append(preprocessed_df['PREPROCESSED_REVIEW'][ind])

print("length of male")
print(len(male))

print("length of female")
print(len(female))

print("length of mixed")
print(len(mixed))


with open('female.pkl', 'wb') as f:
    pickle.dump(female, f)
with open('male.pkl', 'wb') as f:
    pickle.dump(male, f)
with open('mixed.pkl', 'wb') as f:
    pickle.dump(mixed, f)