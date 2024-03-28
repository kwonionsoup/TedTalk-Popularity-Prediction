# CS-7641

## About files:

### Data Folder
- [data_transcript_fully_processed.csv](data/data_transcript_fully_processed.csv) takes the data from [talks_info.csv](data/talks_info.csv) and runs it through the [text processing file](text_processing.py).
- [dropna_processed_deleted_weird.csv](data/dropna_processed_deleted_weird.csv) was my attempt to get rid of the weird line breaks. This file can probably be deleted.
- [talks_info.csv](data/talks_info.csv) is the original dataset from Kaggle. Warning: if you open it with Microsoft Excel, the formatting becomes weird.


### Main Section
- [index.html](index.html) is the webpage that GitHub Pages shows.
- [text_processing.py](text_processing.py) is the final processing code for the data, with the results stored in [data_transcript_fully_processed.csv](data/data_transcript_fully_processed.csv)
- [data_eda.ipynb](data_eda.ipynb) performs exploratory data analysis on the dataset.
- [eda_part2.ipynb](eda_part2.ipynb) performs more exploratory data analysis on the dataset, and focuses on visualizing the distribution of the features.
- [sentiment_analysis_final.ipynb](sentiment_analysis_final.ipynb) is the file with the final version of the two sentiment analysis algorithms (TextBlob and VADER) to be run on our dataset.
- [sentiment_analysis_final.py](sentiment_analysis_final.py) is the same file as above but in .py format.



### Other Folders
- [Maybe_Final_Homework3.ipynb](example_code/Maybe_Final_Homework3.ipynb) (in the example_code folder) is an example of some text generation code that I used in 2021 in case anyone wants a (very basic) reference.
- [preprocess_attempts.ipynb](testing_code_not_final/preprocess_attempts.ipynb) (in the testing_code_not_final folder) is my experimentation that ultimately led to [text_processing.py](text_processing.py)
- [sentiment_analysis.ipynb](testing_code_not_final/sentiment_analysis.ipynb) is a file that experiments with the TextBlob and VADER algorithms on the transcript column of the dataset.
