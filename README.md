# CS-7641 Machine Learning Files

## Main Directory

### Files
- [index.html](index.html): the html code for the GitHub Page
- [requirements.txt](requirements.txt): 


## Models' Folders

### Association Rule Mining (association_mining)
- [association_rule_mining.ipynb](association_mining/association_rule_mining.ipynb): the file that trains and selects hyperparameters for association rule mining
- [association_rule_viz.ipynb](association_mining/association_rule_viz.ipynb): the file that calculates statistics and creates visualizations for word groups extracted from above file
- [association_functions.py](association_mining/association_functions.py): contains helper functions used in association rule mining .ipynb files

### data_preprocessing
- [preprocess.py](data_preprocessing/preprocess.py)
- [preprocess_attempts.ipynb](data_preprocessing/preprocess_attempts.ipynb): the experimentation that ultimately led to [text_processing.py](data_preprocessing/text_processing.py)
- [text_processing.py](data_preprocessing/text_processing.py): the final processing code for the data

### eda
- [data_eda.ipynb](eda/data_eda.ipynb): performs exploratory data analysis on the dataset
- [eda_part2.ipynb](eda/eda_part2.ipynb): performs more exploratory data analysis on the dataset, and focuses on visualizing the distribution of the features

### sentiment_analysis
- [sa_analysis.ipynb](sentiment_analysis/sa_analysis.ipynb): performs analysis on data_sentiment_analysis.csv, which is the dataset that includes TextBlob and VADER scores for each TED Talk.
- [sentiment_analysis_final.ipynb](sentiment_analysis/sentiment_analysis_final.ipynb): the file with the final version of the two sentiment analysis algorithms (TextBlob and VADER) to be run on our dataset
- [sentiment_analysis_final.py](sentiment_analysis/sentiment_analysis_final.py): the same file as [above](sentiment_analysis/sentiment_analysis_final.ipynb) but in .py format
- [sentiment_analysis.ipynb](sentiment_analysis/sentiment_analysis.ipynb) ia file that experiments with the TextBlob and VADER algorithms on the transcript column of the dataset

### svr
- [SVR.ipynb](svr/SVR.ipynb): this is our code-in-progress for support vector regression
- [SVR_Copy.ipynb](svr/SVR_Copy.ipynb)


### Other Folders

#### css
- [style.css](css/style.css): style.css document for our GitHub page

#### data
- [data_sentiment_analysis.csv](data/data_sentiment_analysis.csv) output of sentiment analysis, includes TextBlob and VADER scores.
- [data_title_fully_processed.csv](data/data_title_fully_processed.csv)
- [data_transcript_fully_processed.csv](data/data_transcript_fully_processed.csv) takes the data from [talks_info.csv](data/talks_info.csv) and runs it through the [text processing file](text_processing.py)
- [date_popularity_processed.csv](data/date_popularity_processed.csv)
- [dropna_processed.csv](data/dropna_processed.csv)
- [processed_no_text.csv](data/processed_no_text.csv)
- [talks_info_noedits.csv](data/talks_info_noedits.csv)
- [talks_info.csv](data/talks_info.csv): the original dataset from Kaggle (Warning: if you open it with Microsoft Excel, the formatting becomes weird)

#### pdfs
- [CS_7641_Machine_Learning.pdf](pdfs/CS_7641_Machine_Learning.pdf): project proposal

