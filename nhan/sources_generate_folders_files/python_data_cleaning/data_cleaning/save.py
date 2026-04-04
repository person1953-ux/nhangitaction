import pandas as pd

def save_data(df: pd.DataFrame):
    print("Step 12 - Save clean dataset")
    df.to_csv("clean_sales_data.csv", index=False)
    return df
