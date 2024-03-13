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
def analyze_sentiment(text):
    try:
        blob = TextBlob(text)
        sentiment_score = blob.sentiment.polarity
        return sentiment_score
    except:
        sentiment_score = 0
        return sentiment_score


# In[ ]:


# vader algorithm
sid = SentimentIntensityAnalyzer()


# In[ ]:


# apply textblob algorithm to df and create new column for tb score
df['tb_score'] = df['transcript'].apply(analyze_sentiment)

# apply vader algorithm to df and create new column for vader score
df['vd_score'] = df['transcript'].apply(lambda comments:sid.polarity_scores(str(comments))['compound'])

