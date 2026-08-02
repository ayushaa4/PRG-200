import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Step 1: Load the data
df = pd.read_csv('nepal_bank_transactions.csv')

# what are in the columns and top 5 and last 5 rows
print(df.columns)
print("-"*130)
print(df.head())
print("-"*130)
print(df.tail())
print("-"*130)

# perform generalized statistical analyisis
df.info()
print("-"*130)

# number of rows and columns
print(df.shape)
print("-"*130)

# statistical analysis
print(df.describe())
print("-"*130)

# selecting columns and rows

# select a single columns - return a series
print(df["channel"].head())
print("-"*130)

# select multiple columns - return a dataframe
print(df[["branch_name", "channel", "amount_npr"]].head())
print("-"*130)

# .loc for local-based selection, .iloc for position-based
print(df.loc[0, "branch_name"])
print(df.iloc[0,3])
print("-"*130)

print(df.loc[0:2, ["branch_name", "channel", "transaction_status"]])
print("-"*130)

# filtering with boolean indexing

# All atm cash withdrawals
atm_withdrawals = df[
    (df["channel"] == "ATM") &
    (df["transaction_type"] == "Cash Withdrawal")
]

print(f"ATM cash withdrawals: {len(atm_withdrawals)}")
print(atm_withdrawals.head())
print("-" * 100)

# All failed or reversed transaction
not_successful = df[df["transaction_status"] != "success"]
print(f"Not sucessful: {len(not_successful)} out of {len(df)} ({len(not_successful)/len(df):.1%})")
not_successful["transaction_status"].value_counts()

#High-value fund transfers
large_transfers = df[(df["transaction_type"] == "Fund Transfer") & (df["amount_npr"] >50000)]
print(f"Large fund transfers(> NPR 50,000):{len(large_transfers)}")

# sorting

# top 10 highest_value transactions overall
print(df.sort_values("amount_npr",ascending=False).head(10)[
    ["transaction_id","branch_name","transaction_type","amount_npr","transaction_status"]
])   