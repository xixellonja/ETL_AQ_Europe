import pandas as pd
from rules.columns import extract_columns
from rules.years import filter_not_older_than
from loaders.upload import upload_to_bigquery

# Upload raw data
aq_annual_raw = pd.read_csv("raw_data/aq_annual_raw.csv")


# List of preferred columns to extract
columns_to_extract = ['Sampling Point Id', 'Air Pollutant', 'Air Pollution Level', 'Year', 'Air Quality Station Type', 'Air Quality Station Area', 'Longitude', 'Latitude']

# Extract data and drop NANs/duplicates
aq_annual_clean = extract_columns(aq_annual_raw, columns_to_extract)
aq_annual_clean = aq_annual_clean.dropna().drop_duplicates()

# Filter rows not older than INPUT
aq_annual_clean = filter_not_older_than(aq_annual_clean, 2000, year_col="Year")


# Load clean data
aq_annual_clean.to_csv("cleaned_data/aq_annual_clean.csv", index=False)

upload_to_bigquery(
    csv_path = "cleaned_data/aq_annual_clean.csv",
    table_id = "aq-europe-etl.air_quality.aq_clean"
)

# logs
print("Data extracted")
print(f"Original dataset reduced from {len(aq_annual_raw)} rows to {len(aq_annual_clean)}")


# For debugging
print(aq_annual_clean.isnull().sum())
print(aq_annual_clean.head(5))