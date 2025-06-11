import pandas as pd
from rules.columns import extract_columns

aq_annual_raw = pd.read_csv("raw_data/aq_annual_raw.csv")


# List of preferred columns to extract
columns_to_extract = ['Sampling Point Id', 'Air Pollutant', 'Air Pollution Level', 'Year', 'Air Quality Station Type', 'Air Quality Station Area', 'Longitude', 'Latitude']
aq_annual_clean = extract_columns(aq_annual_raw, columns_to_extract)

# Drop NANs and duplicates
aq_annual_clean = aq_annual_clean.dropna().drop_duplicates()

# Load clean data
aq_annual_clean.to_csv("cleaned_data/aq_annual_clean.csv", index=False)


# For debugging
print(aq_annual_clean.isnull().sum())
print(aq_annual_clean.head(5))
print("Original dataset reduced from " + str(len(aq_annual_raw)) + " rows to " + str(len(aq_annual_clean)) )
print("data extracted")