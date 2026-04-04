import pandas as pd

def standardize_case(df: pd.DataFrame, column: str):
    print("Step 10 - Upper first letter only")
    df[column] = df[column].str.title()
    return df
