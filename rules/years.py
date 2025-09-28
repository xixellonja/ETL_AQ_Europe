# Remove entries not older than a input year
import pandas as pd

def filter_not_older_than(df, min_year, year_col="Year"):
    df = df.copy()
    df[year_col] = pd.to_numeric(df[year_col], errors="coerce")
    df = df.dropna(subset=[year_col])
    return df[df[year_col] >= min_year].reset_index(drop=True)