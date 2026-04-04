import pandas as pd

def replace_values(df: pd.DataFrame):
    print("Step 11 - Replace specific values")
    df = df.replace({"TEXAS":"TX"})
    return df
