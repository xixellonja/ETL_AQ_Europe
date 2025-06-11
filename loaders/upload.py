from google.cloud import bigquery

def upload_to_bigquery(csv_path, table_id):
    client = bigquery.Client()
    print(f"Authenticated project: {client.project}")
    print(f"Uploading file: {csv_path} to table: {table_id}")

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1, # skip header
        autodetect=True,
    )

    with open(csv_path, "rb") as source_file:
        job = client.load_table_from_file(source_file, table_id, job_config=job_config)

    job.result()
    print(f"Uploaded to BigQuery table {table_id}")