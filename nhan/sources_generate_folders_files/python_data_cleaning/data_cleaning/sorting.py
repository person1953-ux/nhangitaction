import pandas as pd

def sort_data(df: pd.DataFrame):
    print("Step 9 - Sort data")
    return df.sort_values(by="purchase_amount", ascending=False)
