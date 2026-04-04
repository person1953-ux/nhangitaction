import pandas as pd

def convert_date(df: pd.DataFrame):
    print("Step 6 - Convert date format")
    df["date"] = pd.to_datetime(df["date"])
    return df
