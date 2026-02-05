import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"

# list files so we know what we're working with
files = sorted([p.name for p in DATA_DIR.glob("*.csv")])
print("CSV files found:", files)

# TODO: replace this with the most "daily activity" looking file after you see the list
# Example (Fitbit-style datasets often have something like "dailyActivity_merged.csv")
filename = files[0]  # temporary
df = pd.read_csv(DATA_DIR / filename)

print("\nUsing file:", filename)
print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())
print("\nHead:")
print(df.head())
