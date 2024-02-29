import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.neighbors import KNeighborsRegressor

def preprocessing(data_file):
    """
    Drops NaN values within the columns "likes", "duration", and "views" of the TED_info data and saves it to a new excel file.

    Args:
        data_file (str): Path to the Excel file
    
    Returns:
        pandas.DataFrame:
    """
    df = pd.read_csv(data_file)
    df = df[['_id', 'duration', 'likes', 'speakers', 'subtitle_languages', 'summary', 'title', 'transcript', 'views', 'recorded_date']]

    print("DF shape:")
    print(df.shape)
    print()

    nan_counts = df.isna().sum()
    print("NaN counts for each column:")
    print(nan_counts)
    print()
    
    # df['likes'] used to be an object data type, not int
    df['likes'] = df['likes'].astype('str')
    df['likes'] = df['likes'].apply(convert_likes)
    print("DF data type:")
    print(df.dtypes)
    print()


    # Drop rows with NaN values
    df_dropna = df.dropna(subset=['likes', 'duration', 'views'])
    df_dropna.to_csv('date_popularity_processed.csv', index=False)
    

    # Unnecessary because there are no NaN values for likes, duration, and views column
    # Fill NaN values with mean
    # imputer = SimpleImputer(strategy='mean')
    # df_mean = df.copy()
    # df_mean[['likes', 'duration', 'views']] = imputer.fit_transform(df_mean[['likes', 'duration', 'views']])
    # df_mean.to_csv('mean_processed.csv', index=False)
    
    # KNN Imputation
    # knn_imputer = KNeighborsRegressor(n_neighbors=5)
    # df_knn = df.copy()
    # df_knn[['likes', 'duration', 'views']] = knn_imputer.fit_transform(df_knn[['likes', 'duration', 'views']])
    # df_knn.to_csv('knn_processed.csv', index=False)


def convert_likes(likes_str):
    # Remove non-numeric characters and convert to numeric
    if likes_str[-1] == 'K':
        return int(float(likes_str.replace('K', '')) * 1000)
    elif likes_str[-1] == 'M':
        return int(float(likes_str.replace('M', '')) * 1000000)
    else:
        return int(likes_str)

def main():
    data_file = 'data/talks_info_noedits.csv'
    df = pd.read_csv(data_file)
    df['recorded_date'] = pd.to_datetime(df['recorded_date'], errors='coerce')
    #Additional Preprocessing
    df1 = pd.read_csv('data/dropna_processed.csv')
    df1 = df1[df1.columns[[0,1,2,8]]]
    df1.insert(2, 'recorded_date', df['recorded_date'], True)
    df1.insert(3, 'popularity', (df1['likes']/df1['views']) * 100, True)
    df1.to_csv('data/date_popularity_processed.csv', index=False)
 

if __name__ == "__main__":
    main()
