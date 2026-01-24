from sqlalchemy import create_engine
import pandas as pd


def main():
  username = "postgres"
  password = "postgres"
  host = "db"
  port = "5432"   
  database = "ny_taxi"

  engine_string = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
  engine = create_engine(engine_string)
  
  try:
    tripdata_df = pd.read_parquet("/data/green_tripdata.parquet")
    tripdata_df.to_sql("tripdata", con=engine, if_exists="fail")
  except Exception as e:
    print("error on: tripdata error on load", e)

  try:
    zone_lookups = pd.read_csv("/data/taxi_zone.csv")
    zone_lookups.to_sql("taxi_zone", con=engine, if_exists="fail")
  except Exception as e:
    print("error on: taxi_zone_lookup error on load", e)
    
if __name__ == "__main__":
  main()