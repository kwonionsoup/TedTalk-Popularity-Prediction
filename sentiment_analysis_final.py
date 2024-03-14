#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
from textblob import TextBlob
import nltk
nltk.download('vader_lexicon')
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# In[ ]:


# textblob algorithm
def textblob(text):
    try:
        blob = TextBlob(text)
        sentiment_score = blob.sentiment.polarity
        return sentiment_score
    except:
        sentiment_score = 0
        return sentiment_score
    

# In[ ]:


# vader algorithm
def vader(df):
    sia = SentimentIntensityAnalyzer()
    # apply vader algorithm to df and create new column for vader score
    return df['processed_transcript'].apply(lambda comments:sia.polarity_scores(str(comments))['compound'])
    

# In[ ]:

def main():
    df = pd.read_csv("CS-7641\data\data_transcript_fully_processed.csv")
    # apply textblob algorithm to df and create new column for tb score
    df['tb_score'] = df['processed_transcript'].apply(textblob)
    df['vd_score'] = vader(df)
    print(df[0:5])

if __name__ == "__main__":
    main()

