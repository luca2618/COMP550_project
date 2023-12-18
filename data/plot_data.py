import pandas as pd
import json
import math
import matplotlib.pyplot as plt

#-----------------------------Helpers-----------------------------------

def load_df_from_json(filename):
  with open(filename, 'r') as f:
    json_dict = json.load(f)
    df = pd.read_json(json_dict)
  return df

#----------------------------Importing----------------------------------

# ['REVIEW_ID', 'USER_ID', 'BOOK_ID', 'BOOK_TITLE', 'PROTAGONIST',
#      'DATE_PUBLISHED', 'DATE_READ', 'AVG_RATING', 'RATING']
meta_df = pd.read_csv('meta_dataset.csv')

# ['REVIEW_ID', 'PROTAGONIST', 'REVIEW']
reviews_df = pd.read_csv('reviews_dataset.csv')

# ['REVIEW_ID', 'PROTAGONIST', 'PREPROCESSED_REVIEW']
preprocessed_df = load_df_from_json('preprocessed_reviews_dataset.json')

# ['BOOK_ID', 'BOOK_TITLE', 'PROTAGONIST', 'DATE_PUBLISHED', 'AVG_RATING',
#      'REVIEW_COUNT', 'MAIN_PROTAGONIST']
books_df = pd.read_csv('books_dataset.csv')

#----------------------------Plotting-----------------------------------

# books_df = meta_df.groupby(['BOOK_ID', 'BOOK_TITLE', "PROTAGONIST", "DATE_PUBLISHED", "AVG_RATING"]).size().reset_index(name='REVIEW_COUNT')
# print(books_df)

#----------------------------Plot 1-------------------------------------
# This plot assumes that the review refers to the main character by their first name
# Plot percentage of reviews contain a reference to the main character

first_names = books_df["MAIN_PROTAGONIST"].str.split().str[0]

cp_books = pd.concat([books_df.drop(["MAIN_PROTAGONIST"], axis=1), first_names], axis=1)

cp_reviews = pd.merge(reviews_df, meta_df, on="REVIEW_ID")

print(cp_reviews.columns)

cp_reviews = pd.merge(cp_reviews, cp_books[["BOOK_ID", "MAIN_PROTAGONIST"]], on="BOOK_ID")

def contains_main_character(review_text, main_character):
    return main_character.lower() in review_text.lower()

cp_reviews['CONTAINS'] = cp_reviews.apply(lambda row: contains_main_character(row['REVIEW'], row['MAIN_PROTAGONIST']), axis=1)

print(cp_reviews.columns)
count_reviews_with_main_character = cp_reviews.groupby('BOOK_TITLE')['CONTAINS'].sum().reset_index()

print(count_reviews_with_main_character)

count_reviews = meta_df['BOOK_TITLE'].value_counts().to_frame(name="COUNT")
count_reviews = count_reviews.reset_index().rename(columns={"index":"BOOK_TITLE"})
print(count_reviews)

final = pd.merge(count_reviews, count_reviews_with_main_character, on="BOOK_TITLE")

final["SHORT"] = final["BOOK_TITLE"].str[:10]
final["PERCENT"] = final["CONTAINS"]/final["COUNT"] 
  
final.set_index('SHORT', inplace=True)

fig, ax = plt.subplots()

fig.set_figheight(8)
fig.set_figwidth(14)

bar_width = 0.95
index = range(len(final))

ax.bar(index, final['PERCENT'], bar_width, label='Reviews mentioning MC')

# ax.bar([i + bar_width for i in index], final['COUNT'], bar_width, label='Reviews')

ax.set_xlabel('Titles')
ax.set_ylabel('Percentage')
# ax.set_title('')
ax.set_xticks([i + bar_width / 2 for i in index])
ax.set_xticklabels(final.index, rotation='vertical')
# ax.legend()

plt.tight_layout()

plt.savefig("plot.png")
# Show the plot
plt.show()

# filtered_reviews = reviews_df[reviews_df['REVIEW'].str.contains(specified_word, case=False)]