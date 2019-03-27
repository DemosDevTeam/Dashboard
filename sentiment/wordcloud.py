import pandas as pd 
import numpy as numpy
import matplotlib.pyplot as plt

import nltk
from nltk.corpus import stopwords
from nltk.classify import SklearnClassifier 
from sklearn.model_selection import train_test_split

import wordcloud

# df = pd.read_csv("data/csv/residentResponses.csv")
df = df[['text', 'sentiment']]

train, test = train_test_split(df, test_size = 0.1)
# Removing neutral sentiments
train = train[train.sentiment != "Neutral"]

train_pos = train[ train['sentiment'] == 'Positive']
train_pos = train_pos['text']
train_neg = train[ train['sentiment'] == 'Negative']
train_neg = train_neg['text']

def wordcloud_draw(data, color = 'black'):
    words = ' '.join(data)
    cleaned_word = " ".join([word for word in words.split()
                            if 'http' not in word
                                and not word.startswith('@')
                                and not word.startswith('#')
                                and word != 'RT'
                            ])
    wordcloud = wordcloud.WordCloud(stopwords=wordcloud.STOPWORDS,
                      background_color=color,
                      width=2500,
                      height=2000
                     ).generate(cleaned_word)
    plt.figure(1,figsize=(13, 13))
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()
    
print("Positive words")
wordcloud_draw(train_pos,'white')
print("Negative words")
wordcloud_draw(train_neg)
print('urets')