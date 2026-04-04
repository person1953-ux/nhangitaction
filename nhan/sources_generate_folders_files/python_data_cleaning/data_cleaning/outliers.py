import pandas as pd

def remove_outliers(df: pd.DataFrame):
    print("Step 7 - Detect outliers using IQR")
    Q1 = df["purchase_amount"].quantile(0.25)
    Q3 = df["purchase_amount"].quantile(0.75)
    IQR = Q3 - Q1
    return df
