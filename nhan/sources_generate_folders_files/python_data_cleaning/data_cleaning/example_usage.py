import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from data_cleaning.explore import explore_data
from data_cleaning.deduplicate import remove_duplicates
from data_cleaning.clean_text import clean_text
from data_cleaning.handle_missing import handle_missing
from data_cleaning.convert_types import convert_types
from data_cleaning.convert_date import convert_date
from data_cleaning.outliers import remove_outliers
from data_cleaning.create_features import create_features
from data_cleaning.sorting import sort_data
from data_cleaning.standardize_case import standardize_case
from data_cleaning.replace_values import replace_values
from data_cleaning.save import save_data

# ----------------------------
# Create a dummy dataset
# ----------------------------
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, None, 30],
    "purchase_amount": [100, 200, 150],
    "country": ["CANADA", "usa", "Mexico"],
    "state": ["TEXAS", "California", "NY"],
    "date": ["2023-01-01","2023-02-01","2023-03-01"],
    "email": ["alice@email.com", None, "charlie@email.com"]
})

# ----------------------------
# Run the full data cleaning pipeline
# ----------------------------
print("Step 1: Exploring data")
df = explore_data(df)                               # Step 1
print("Step 2: Removing duplicates")
df = remove_duplicates(df)                          # Step 2
print("Step 3: Cleaning text")
df = clean_text(df, "name")                         # Step 3
print("Step 4: Handling missing values")
df = handle_missing(df)                             # Step 4
print("Step 5: Converting types")
df = convert_types(df)                              # Step 5
print("Step 6: Converting dates")
df = convert_date(df)                               # Step 6
print("Step 7: Removing outliers")
df = remove_outliers(df)                            # Step 7
print("Step 8: Creating features")
df = create_features(df)                            # Step 8
print("Step 9: Sorting data")
df = sort_data(df)                                  # Step 9
print("Step 10: Standardizing case")
df = standardize_case(df, "country")               # Step 10
print("Step 11: Replacing values")
df = replace_values(df)                             # Step 11
print("Step 12: Saving data")
df = save_data(df)                                  # Step 12

print("Pipeline completed. Clean dataset saved as clean_sales_data.csv")