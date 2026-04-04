import pandas as pd

def create_features(df: pd.DataFrame):
    print("Step 8 - Create new features")
    df["purchase_category"] = df["purchase_amount"].apply(lambda x: "High" if x  else "Low")
    return df
