
from google.cloud import storage, bigquery

PROJECT_ID = "sublime-seat-484418-h6"
DATASET_ID = "dezoomcamp_hw3_2025"
TABLE_ID = "yellow_tripdata_2024_ext"

CREDENTIALS_FILE = "credentials.json"

GCS_BUCKET = "sublime-seat-484418-dezoomcamp_hw3_2025"
GCS_PREFIX = "yellow_tripdata_2024" 

def table_exists(bq: bigquery.Client, dataset_id: str, table_id: str) -> bool:
    try:
        bq.get_table(f"{bq.project}.{dataset_id}.{table_id}")
        return True
    except Exception:
        return False
    
def get_source_uris_from_gcs(bucket_name: str, prefix: str = "", suffix: str = ".parquet") -> list[str]:
    storage_client = storage.Client.from_service_account_json(
        CREDENTIALS_FILE, project=PROJECT_ID
    )
    bucket = storage_client.bucket(bucket_name)

    uris: list[str] = []
    for blob in storage_client.list_blobs(bucket, prefix=prefix):
        if suffix and not blob.name.endswith(suffix):
            continue
        uris.append(f"gs://{bucket_name}/{blob.name}")

    if not uris:
        raise ValueError(f"No matching objects found in gs://{bucket_name}/{prefix} (suffix={suffix})")

    return uris

def create_external_table(dataset_id: str, table_id: str, source_uris: list[str]):
    bq = bigquery.Client.from_service_account_json(CREDENTIALS_FILE, project=PROJECT_ID)

    if table_exists(bq, dataset_id, table_id):
        print(f"External table already exists: {bq.project}.{dataset_id}.{table_id} (skipping)")
        return
    
    table_ref = bigquery.DatasetReference(bq.project, dataset_id).table(table_id)

    external_config = bigquery.ExternalConfig("PARQUET")
    external_config.source_uris = source_uris
    external_config.autodetect = True

    table = bigquery.Table(table_ref)
    table.external_data_configuration = external_config

    bq.delete_table(table_ref, not_found_ok=True)
    bq.create_table(table)
    print(f"Created external table: {bq.project}.{dataset_id}.{table_id}")


def create_native_table_from_external(
    dataset_id: str,
    external_table_id: str,
    native_table_id: str | None = None,
):
    bq = bigquery.Client.from_service_account_json(CREDENTIALS_FILE, project=PROJECT_ID)

    if native_table_id is None:
        native_table_id = f"{external_table_id}_native"

    if table_exists(bq, dataset_id, native_table_id):
        print(f"Native table already exists: {bq.project}.{dataset_id}.{native_table_id} (skipping)")
        return

    # CTAS from the external table
    sql = f"""
        CREATE TABLE `{bq.project}.{dataset_id}.{native_table_id}` AS
        SELECT * FROM `{bq.project}.{dataset_id}.{external_table_id}`
    """
    job = bq.query(sql)
    job.result()

    print(f"Created native table: {bq.project}.{dataset_id}.{native_table_id}")


if __name__ == "__main__":
    source_uris = get_source_uris_from_gcs(GCS_BUCKET, prefix=GCS_PREFIX, suffix=".parquet")
    
    create_external_table(DATASET_ID, TABLE_ID, source_uris)
    
    create_native_table_from_external(DATASET_ID, TABLE_ID, f"{TABLE_ID}_native")