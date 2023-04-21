import glob
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Get a list of all CSV files in the folder
csv_files = glob.glob("*.csv")


# Loop over each CSV file and replace "?" with column mean
for csv_file in csv_files:
    # Read the CSV file into a pandas dataframe
    df = pd.read_csv(csv_file)

    # Replace all "?" with NaN
    df = df.replace('?', np.nan)

    # Find columns with headers that start with lowercase and end with 'X'
    lowercase_cols = [col for col in df.columns if col.strip()[0].islower()]

    # Replace lowercase 'X' columns with mode of column
    for col in lowercase_cols:
        mode_val = df[col].mode()[0]  # get mode of column
        df[col] = df[col].fillna(mode_val)  # replace NaN values with mode value

    le = LabelEncoder()
    for sym in lowercase_cols:
        col = le.fit_transform(df[sym])
        df[sym] = col.copy()

    # Replace all other columns with their mean
    other_cols = [col for col in df.columns if col not in lowercase_cols]

    for col in other_cols:
        df[col] = df[col].astype(float)
    means = df[other_cols].mean()
    df[other_cols] = df[other_cols].fillna(means)

    # Write the updated dataframe back to the CSV file
    df.to_csv(csv_file, index=False)
