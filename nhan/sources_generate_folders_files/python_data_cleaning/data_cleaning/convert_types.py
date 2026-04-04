import pandas as pd

def convert_types(df: pd.DataFrame):
    print("Step 5 - Convert data types")
    df["purchase_amount"] = pd.to_numeric(df["purchase_amount"], errors="coerce")
    df["purchase_amount"] = df["purchase_amount"].fillna(df["purchase_amount"].median())
    return df
