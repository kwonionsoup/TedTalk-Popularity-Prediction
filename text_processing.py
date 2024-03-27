import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
import contractions
import string
import ast

# global vars
stopws = stopwords.words("english")

def michael_preprocess(data_file):
    """
    Drops NaN values within the columns "likes", "duration", and "views" of the TED_info data and saves it to a new excel file.

    Args:
        data_file (str): Path to the Excel file
    
    Returns:
        pandas.DataFrame:
    """

    df = pd.read_csv(data_file)
    df = df[['_id', 'duration', 'likes', 'speakers', 'subtitle_languages', 'summary', 'topics', 'title', 'transcript', 'views', 'recorded_date', 'published_date']]

    # add published date
    df['published_date'] = pd.to_datetime(df['published_date'], errors='coerce').dt.date
    
    # df['likes'] used to be an object data type, not int
    df['likes'] = df['likes'].astype('str')
    df['likes'] = df['likes'].apply(convert_likes)
   
    # Drop rows with NaN values
    df_dropna = df.dropna(subset=['likes', 'duration', 'views'])

    return df_dropna

def convert_likes(likes_str):
    # Remove non-numeric characters and convert to numeric
    if likes_str.endswith('K'):
        return int(float(likes_str.replace('K', '')) * 1000)
    elif likes_str.endswith('M'):
        return int(float(likes_str.replace('M', '')) * 1000000)
    else:
        return int(likes_str)

def convert_dictionaires(df):

    final_df = df.copy()

    #  Now I want to be able to use the values in speakers, subtitle languages, and topics, so let's change those dictionaries into lists
    final_df['speakers'] = final_df['speakers'].apply(ast.literal_eval)
    # edit speakers column to make a list of topics instead of a dictionary of topics
    final_df['speakers_list'] = final_df['speakers'].apply(lambda x: [topic['name'] for topic in x])
    
    final_df['subtitle_languages'] = final_df['subtitle_languages'].apply(ast.literal_eval)
    # edit subtitle langauages column to make a list of topics instead of a dictionary of topics
    final_df['sl_list'] = final_df['subtitle_languages'].apply(lambda x: [topic['name'] for topic in x])
    
    final_df['topics'] = final_df['topics'].apply(ast.literal_eval)
    # edit topics column to make a list of topics instead of a dictionary of topics
    final_df['topics_list'] = final_df['topics'].apply(lambda x: [topic['name'] for topic in x])
    
    # Let's view the dataset again
    final_df.head()

    return final_df


def main():

    data_path = 'data/talks_info.csv'

    df = michael_preprocess(data_path)
    # df = df_org[['_id', 'duration', 'likes', 'speakers', 'subtitle_languages', 'summary', 'title', 'transcript', 'views', 'recorded_date']]
    df["transcript"] = df.transcript.astype("string")

    # final_transcript = df.copy()
    final_transcript = convert_dictionaires(df)
    final_transcript.fillna("nan",inplace=True)
    final_transcript["processed_transcript"] = final_transcript["transcript"].apply(process_text)
    # final_transcript["transcript_no_contractions"] = final_transcript["transcript"].apply(process_text2)
    # final_transcript["processed_title"] = final_transcript["title"].apply(process_text)

    final_transcript.to_csv("data/data_transcript_fully_processed.csv")

    
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

    # fix us and vs
    removed_us = ['uss' if word=='us' else word for word in removed]
    removed_vs = ['vss' if word=='us' else word for word in removed_us]

    # lemmatization
    lemm = WordNetLemmatizer()
    lemmed = [lemm.lemmatize(word) for word in removed_vs]
    
    # put string together
    final_text = " ".join(lemmed)

    return final_text

def process_text2(conversation):
    
    if conversation!='nan':
        contractions_stuff = [contractions.fix(word) for word in conversation.split()]
        conversation = ' '.join(contractions_stuff)
        
    return conversation


if __name__ == "__main__":
    main()
