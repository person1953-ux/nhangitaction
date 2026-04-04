import pandas as pd

def explore_data(df: pd.DataFrame):
    print("Step 1 - Explore the Data")
    print(df.head())
    print(df.info())
    print(df.describe())
    print(df.isnull().sum())
    return df
