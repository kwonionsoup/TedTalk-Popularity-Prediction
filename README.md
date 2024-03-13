# CS-7641

## About files:

### Data Folder
- [data_transcript_fully_processed.csv](data/data_transcript_fully_processed.csv) takes the data from [talks_info.csv](data/talks_info.csv) and runs it through the [text processing file](text_processing.py].
- [dropna_processed_deleted_weird.csv](data/dropna_processed_deleted_weird.csv) was my attempt to get rid of the weird line breaks. This file can probably be deleted.
- [talks_info.csv](data/talks_info.csv) is the original dataset from Kaggle. Warning: if you open it with Microsoft Excel, the formatting becomes weird.


### Main Section
- [index.html](index.html) is the webpage that GitHub Pages shows.
- [text_processing.py](text_processing.py) is the final processing code for the data, with the results stored in [data_transcript_fully_processed.csv](data/data_transcript_fully_processed.csv)
- [data_eda.ipynb](data_eda.ipynb) performs exploratory data analysis on the dataset.



### Other Folders
- [Maybe_Final_Homework3.ipynb](example_code/Maybe_Final_Homework3.ipynb) (in the example_code folder) is an example of some text generation code that I used in 2021 in case anyone wants a (very basic) reference.
- [preprocess_attempts.ipynb](testing_code_not_final/preprocess_attempts.ipynb) (in the testing_code_not_final folder) is my experimentation that ultimately led to [text_processing.py](text_processing.py)
