

# Remove columns by default, if more than 25% of the data is missing 
def remove_25_percent(df):
    max = len(df) * 0.25
    for column in df.columns:
         total_nulls = df[column].isnull().sum()
         if total_nulls >= max:
            data = df.drop(columns=[column])
    return data


# Remove <25% and selected columns
def extract_columns(df, columns_to_extract):
    data = remove_25_percent(df)
    data = data[columns_to_extract]
    return data

