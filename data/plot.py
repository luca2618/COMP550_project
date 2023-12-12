import pandas as pd
import math
import matplotlib.pyplot as plt

#['REVIEW_ID', 'USER_ID', 'BOOK_ID', 'BOOK_TITLE', 'PROTAGONIST',
#      'REVIEW', 'RATING', 'RATING_DIST', 'DATE_PUBLISHED', 'DATE_READ']
reviews_df = pd.read_csv('data/goodreads_reviews_dataset.csv')

### counting genders of protagonists

#reviews_df = reviews_df[reviews_df["REVIEW"].str.len() > 500]

books_df = reviews_df.groupby(['BOOK_ID', 'BOOK_TITLE', "DATE_PUBLISHED"]).size().reset_index(name='review_count')

print(books_df)

books_df.to_csv("books_dataset.csv", index=False)

genders = reviews_df['PROTAGONIST'].values.tolist()

print(f'Female-led: {genders.count("F")}')
print(f'Male-led: {genders.count("M")}')
print(f'Other: {genders.count("Various (M and F)")}')
print(f'\nTotal reviews: {len(genders)}')


#testing
test_title = "The Fault in Our Stars"
df = reviews_df[reviews_df["BOOK_TITLE"] == test_title]

print(df)

search = "intelligent"
df = df[df["REVIEW"].str.contains(search, case=False, na=False)]

# df = df[df["REVIEW"].str.len() == ]

print(df["REVIEW"])
kr = df["REVIEW"]

# kr.to_csv("hazel.csv")