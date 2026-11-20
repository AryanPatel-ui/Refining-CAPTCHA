import pandas as pd

df = pd.read_csv("captcha_dataset.csv")

print("Dataset information:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

print("\nStatistical summary:")
print(df.describe())

print("\nHuman/Bot distribution:")
print(df["label"].value_counts())

print("\nDuplicate rows:")
print(df.duplicated().sum())