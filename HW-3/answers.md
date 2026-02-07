1. Running the query inside GCP UI:

```
SELECT count(*) 
FROM `sublime-seat-484418-h6.dezoomcamp_hw3_2025.yellow_tripdata_2024_ext`;
```
it should return 20332093.

2. Doing agains the standard/native materialized table:

```
SELECT DISTINCT PULocationID 
FROM `sublime-seat-484418-h6.dezoomcamp_hw3_2025.yellow_tripdata_2024_ext_native`;
```

will output "Esta consulta procesará 155.12 MB cuando se ejecute.
Esta consulta procesará 155.12 MB cuando se ejecute." (spanish), so the answer is 0 and 155.12MB.

3. 

Option A:
```
SELECT PULocationID 
FROM `sublime-seat-484418-h6.dezoomcamp_hw3_2025.yellow_tripdata_2024_ext_native`;
```
Stimated: 155.12 MB.

Option B:

```
SELECT PULocationID, DOLocationID 
FROM `sublime-seat-484418-h6.dezoomcamp_hw3_2025.yellow_tripdata_2024_ext_native`;
```
Stimated: 310.24 MB.

My guess is that since the storage is columnar, obviously bringing two columns will double the amount of size. In this case both columns have the same type so it will be exactly twice the amount of data.
Answer n°1 aligns with this thinking.

4. 
```
SELECT count(fare_amount)
FROM `sublime-seat-484418-h6.dezoomcamp_hw3_2025.yellow_tripdata_2024_ext_native`
WHERE fare_amount = 0
;
```

Output: 8333

5.

Partition always by date (in this case tpep_dropoff_datetime), then cluster by the vendorID such that the data related to that vendor id is closer inside the storage (local proximity or something like that). So the first option is correct. Here's the SQL:

```
CREATE OR REPLACE TABLE `sublime-seat-484418-h6.dezoomcamp_hw3_2025.yellow_tripdata_2024_partitioned`
PARTITION BY DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID
AS
SELECT * 
FROM `sublime-seat-484418-h6.dezoomcamp_hw3_2025.yellow_tripdata_2024_ext_native`;
```
It read around 2.7 GB of data.

6.

Using standard table:

```
SELECT DISTINCT VendorID 
FROM `sublime-seat-484418-h6.dezoomcamp_hw3_2025.yellow_tripdata_2024_ext_native`
WHERE tpep_dropoff_datetime BETWEEN "2024-03-01" AND "2024-03-15" 
;
```
Output: 310.24 MB

Using partition + cluster table:

```
SELECT DISTINCT VendorID 
FROM `sublime-seat-484418-h6.dezoomcamp_hw3_2025.yellow_tripdata_2024_partitioned`
WHERE tpep_dropoff_datetime BETWEEN "2024-03-01" AND "2024-03-15" 
;
```
Output: 26.84 MB

8. False, as it's not always the best practice, e.g., small tables don't need it.

7. GCP Bucket