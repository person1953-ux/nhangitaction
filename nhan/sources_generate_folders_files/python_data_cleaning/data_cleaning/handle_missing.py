import pandas as pd

def handle_missing(df: pd.DataFrame):
    print("Step 4 - Handle missing values")
    df["age"] = df["age"].fillna(df["age"].mean())
    df["email"] = df["email"].fillna("unknown@email.com")
    return df
