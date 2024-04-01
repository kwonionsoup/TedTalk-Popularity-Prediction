# CS-7641

## About files:

### Main Directory
- [association_rule_mining.ipynb](association_rule_mining.ipynb): the file that trains and selects hyperparameters for association rule mining
- [association_rule_viz.ipynb](association_rule_viz.ipynb): the file that calculates statistics and creates visualizations for word groups extracted from above file
- [association_functions.py](association_functions.py): contains helper functions used in association rule mining .ipynb files
- [data_eda.ipynb](data_eda.ipynb): performs exploratory data analysis on the dataset
- [eda_part2.ipynb](eda_part2.ipynb): performs more exploratory data analysis on the dataset, and focuses on visualizing the distribution of the features
- [index.html](index.html): the html code for the GitHub Page
- [requirements.txt](requirements.txt): 
- [sa_analysis.ipynb](sa_analysis.ipynb): 
- [sentiment_analysis_final.ipynb](sentiment_analysis_final.ipynb): the file with the final version of the two sentiment analysis algorithms (TextBlob and VADER) to be run on our dataset
- [sentiment_analysis_final.py](sentiment_analysis_final.py): the same file as [above](sentiment_analysis_final.ipynb) but in .py format
- [SVR.ipynb](SVR.ipynb): this is our code-in-progress for support vector regression
- [text_processing.py](text_processing.py): the final processing code for the data


### Data Folder
- [data_sentiment_analysis.csv](data/data_sentiment_analysis.csv)
- [data_title_fully_processed.csv](data/data_title_fully_processed.csv)
- [data_transcript_fully_processed.csv](data/data_transcript_fully_processed.csv) takes the data from [talks_info.csv](data/talks_info.csv) and runs it through the [text processing file](text_processing.py)
- [date_popularity_processed.csv](data/date_popularity_processed.csv)
- [dropna_processed.csv](data/dropna_processed.csv)
- [preprocess.py](data/preprocess.py)
- [processed_no_text.csv](data/processed_no_text.csv)
- [talks_info_noedits.csv](data/talks_info_noedits.csv)
- [talks_info.csv](data/talks_info.csv): the original dataset from Kaggle (Warning: if you open it with Microsoft Excel, the formatting becomes weird)


### Other Folders

#### css
- [style.css](css/style.css): style.css document for our GitHub page

#### example_code
- [Maybe_Final_Homework3.ipynb](example_code/Maybe_Final_Homework3.ipynb): an example of some text generation code that I used in 2021 in case anyone wants a (very basic) reference

#### pdfs
- [CS_7641_Machine_Learning.pdf](pdfs/CS_7641_Machine_Learning.pdf): project proposal


#### testing_code_not_final
- [preprocess_attempts.ipynb](testing_code_not_final/preprocess_attempts.ipynb): the experimentation that ultimately led to [text_processing.py](text_processing.py)
- [sentiment_analysis.ipynb](testing_code_not_final/sentiment_analysis.ipynb) ia file that experiments with the TextBlob and VADER algorithms on the transcript column of the dataset
- [SVR.ipynb](testing_code_not_final/SVR.ipynb)
