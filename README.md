# CS-7641 Machine Learning Files

## Main Directory

- [index.html](index.html): the html code for the GitHub Page
- [requirements.txt](requirements.txt): list of required Python packages for the repository


## Models' Folders

### association_mining
Folder containing Association Rule Mining code
- [association_rule_mining.ipynb](association_mining/association_rule_mining.ipynb): the file that trains and selects hyperparameters for association rule mining
- [association_rule_viz.ipynb](association_mining/association_rule_viz.ipynb): the file that calculates statistics and creates visualizations for word groups extracted from above file
- [association_functions.py](association_mining/association_functions.py): contains helper functions used in association rule mining .ipynb files

### data_preprocessing
Folder containing Data Preprocessing code
- [preprocess.py](data_preprocessing/preprocess.py): beginning data preprocessing code
- [preprocess_attempts.ipynb](data_preprocessing/preprocess_attempts.ipynb): the experimentation that ultimately led to [text_processing.py](data_preprocessing/text_processing.py)
- [text_processing.py](data_preprocessing/text_processing.py): the final processing code for the data

### eda
Folder containing EDA code
- [data_eda.ipynb](eda/data_eda.ipynb): performs exploratory data analysis on the dataset
- [eda_part2.ipynb](eda/eda_part2.ipynb): performs more exploratory data analysis on the dataset, and focuses on visualizing the distribution of the features

### sentiment_analysis
Folder containing Sentiment Analysis code
- [emotion_detection.py](sentiment_analysis/emotion_detection.py): implementation of emotion detection
- [sa_analysis.ipynb](sentiment_analysis/sa_analysis.ipynb): performs analysis on [data_sentiment_analysis.csv](data/data_sentiment_analysis.csv), which is the dataset that includes TextBlob and VADER scores for each TED Talk.
- [sentiment_analysis_final.ipynb](sentiment_analysis/sentiment_analysis_final.ipynb): the file with the final version of the two sentiment analysis algorithms (TextBlob and VADER) to be run on our dataset
- [sentiment_analysis_final.py](sentiment_analysis/sentiment_analysis_final.py): the same file as [above](sentiment_analysis/sentiment_analysis_final.ipynb) but in .py format
- [sentiment_analysis.ipynb](sentiment_analysis/sentiment_analysis.ipynb) ia file that experiments with the TextBlob and VADER algorithms on the transcript column of the dataset

### svr
Folder containing SVR code
- [SVR.ipynb](svr/SVR.ipynb): this is our code-in-progress for support vector regression
- [SVR_Copy.ipynb](svr/SVR_copy.ipynb)

### text gen
Folder containing Text Generation code
- [text_gen.ipynb](text_gen/text_gen.ipynb): explores 4 different encoder-decoder text summarization models without fine-tuning

## Other Folders

### css
Folder containing CSS code
- [style.css](css/style.css): style.css document for our GitHub page

### data
Folder containing data
- [data_sentiment_analysis.csv](data/data_sentiment_analysis.csv) output of sentiment analysis, includes TextBlob and VADER scores
- [data_title_fully_processed.csv](data/data_title_fully_processed.csv): file with a processed title field
- [data_transcript_fully_processed.csv](data/data_transcript_fully_processed.csv) takes the data (specifically the transcript) from [talks_info.csv](data/talks_info.csv) and runs it through the [text processing file](text_processing.py)
- [date_popularity_processed.csv](data/date_popularity_processed.csv): file with popularity and processed data
- [talks_info.csv](data/talks_info.csv): the original dataset from Kaggle (Warning: if you open it with Microsoft Excel, the formatting becomes weird)
- [updated_transcripts_with_emotions_final.csv](data/updated_transcripts_with_emotions_final.csv): contains transcripts with detected emotions extracted using OpenAI API and prompt engineering, not ready for SVR model integration yet.
- [final_data_for_svr.csv](data/final_data_for_svr.csv): Combined data_sentiment_analysis.csv and updated_transcripts_with_emotions_final.csv and ready to be used for SVR model.

### pdfs
Folder containing pdfs
- [proposal.pdf](pdfs/proposal.pdf): project proposal
- [midterm_report.pdf](pdfs/midterm_report.pdf): midterm report

<!-- - [talks_info_noedits.csv](data/talks_info_noedits.csv) -->
<!-- - [dropna_processed.csv](data/dropna_processed.csv)
- [processed_no_text.csv](data/processed_no_text.csv) -->