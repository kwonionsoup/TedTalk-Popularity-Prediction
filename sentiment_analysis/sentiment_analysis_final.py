#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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
    data_sentiment_analysis = pd.read_csv("CS-7641\data\data_transcript_fully_processed.csv")
    # apply textblob algorithm to df and create new column for tb score
    data_sentiment_analysis['tb_score'] = data_sentiment_analysis['processed_transcript'].apply(textblob)
    data_sentiment_analysis['vd_score'] = vader(data_sentiment_analysis)
    print(data_sentiment_analysis[0:5])
    data_sentiment_analysis.to_csv('CS-7641\data\data_sentiment_analysis.csv')

if __name__ == "__main__":
    main()

