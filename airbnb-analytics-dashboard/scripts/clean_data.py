"""
clean_data.py

Cleans and enriches the raw Airbnb listings data for use in Power BI.

Run:
    python clean_data.py

Input:
    data/raw/listings.csv

Output:
    data/processed/listings_clean.csv
"""

import pandas as pd
import numpy as np

df = pd.read_csv("data/raw/listings.csv")

# --- Basic cleaning ---
df = df.drop_duplicates(subset="id")
df = df[df["price"] > 0]

# Cap extreme outliers at the 99th percentile so charts aren't skewed
price_cap = df["price"].quantile(0.99)
df["price"] = np.where(df["price"] > price_cap, price_cap, df["price"])

# Fill missing review activity with 0 rather than blank
df["reviews_per_month"] = df["reviews_per_month"].fillna(0)
df["number_of_reviews"] = df["number_of_reviews"].fillna(0)

# --- Derived fields useful for Power BI visuals ---
df["price_per_night_bucket"] = pd.cut(
    df["price"],
    bins=[0, 75, 150, 250, 400, np.inf],
    labels=["$0-75", "$75-150", "$150-250", "$250-400", "$400+"],
)

df["is_superhost"] = df["host_is_superhost"].map({"t": True, "f": False})

df["last_review"] = pd.to_datetime(df["last_review"], errors="coerce")
df["days_since_last_review"] = (pd.Timestamp("2026-09-04") - df["last_review"]).dt.days

df["availability_status"] = pd.cut(
    df["availability_365"],
    bins=[-1, 30, 180, 365],
    labels=["Rarely Available", "Sometimes Available", "Highly Available"],
)

df.to_csv("data/processed/listings_clean.csv", index=False)
print(f"Cleaned data written to data/processed/listings_clean.csv ({len(df)} rows)")
