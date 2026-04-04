import pandas as pd

def remove_duplicates(df: pd.DataFrame):
    print("Step 2 - Remove duplicates")
    return df.drop_duplicates()
