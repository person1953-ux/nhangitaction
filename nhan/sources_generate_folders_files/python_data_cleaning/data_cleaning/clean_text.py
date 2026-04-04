import pandas as pd

def clean_text(df: pd.DataFrame, column: str):
    print("Step 3 - Clean space in text columns")
    df[column] = df[column].str.strip()
    return df
