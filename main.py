#IMPPORT LIBRARIES AND DATASET

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

#Importing Dataset

ratings_df = pd.read_csv('rating.csv')
ratings_df.head()

#Imorting the movies datase4t from where we have got rhe ratings

movies_df = pd.read_csv('movies.csv')
movies_df.head()

#DATA PREPROCESSING

"""In movies dataset we have year along the titel"""
"""So first we will extract year from titel and assign it to a new column"""

movies_df['year'] = movies_df.title.str.exract('(\(\d\d\d\d))', expand = True)
movies_df.head()

#Remove parantheses from year

movies_df['title'] = movies_df.title.str.replace('(\d\d\d\d\)', expand=True)
movies_df.head()

#Remo

movies_df['title'] = movies_df.title.str.replace('(\(\d\d\d\d\))', '')
movies_df.head()

#Remove all the whitespaces from title

movies_df['title'] = movies_df['title'].apply(lambda x: x.strip())

#Convert Geres into a list

movies_df['genres'] = movies_df.genres.str,split('|')
movies_df.head()

#One Hot Encoding of Genres

movies_copy = movies_df.copy()

for index, row in movies_df.iterrows():
    for genre in row['genres']:
        movies_copy.at[index, genre] = 1

        movies_copy.head()

        #Filling NAN values with 0