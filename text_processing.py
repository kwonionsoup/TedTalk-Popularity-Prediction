import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
import contractions

import string

df_org = pd.read_csv("data/talks_info_noedits.csv")
df = df_org[['_id', 'duration', 'likes', 'speakers', 'subtitle_languages', 'summary', 'title', 'transcript', 'views', 'recorded_date']]
df["transcript"] = df.transcript.astype("string")

stopws = stopwords.words("english")
def process_text(conversation):
    
    # expand contractions
    contractions_stuff = [contractions.fix(word) for word in conversation.split()]
    conversation = ' '.join(contractions_stuff)
    
    # convert to lowercase
    conversation = conversation.lower()
    
    # remove punctuation
    convo = "".join([char for char in conversation if char not in string.punctuation])
    
    # tokenize words
    words_tok = word_tokenize(convo)
    
    # remove stopwords
    removed = [word for word in words_tok if word not in stopws]

    # lemmatization
    lemm = WordNetLemmatizer()
    lemmed = [lemm.lemmatize(word) for word in removed]
    
    # put string together
    final_text = " ".join(lemmed)

    return final_text

transcript1 = df[df["_id"]=="21"]["transcript"]
print(process_text(transcript1[0]))