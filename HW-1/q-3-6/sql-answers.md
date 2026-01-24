3. 8,007

```
SELECT count(*)
FROM tripdata
WHERE (lpep_pickup_datetime >= '2025-11-01' AND 
	   lpep_pickup_datetime < '2025-12-01') AND
	trip_distance <= 1;
```

4. 2025-11-14 15:36:27

```
SELECT index, lpep_pickup_datetime, trip_distance
FROM tripdata
WHERE trip_distance <= 100
ORDER BY trip_distance DESC LIMIT 5;
```
5. East Harlem North

```
SELECT "PULocationID", sum(total_amount) as amount_per_location
FROM tripdata
GROUP BY "PULocationID"
ORDER BY amount_per_location DESC LIMIT 5;


SELECT index, "Zone"
FROM taxi_zone
WHERE "LocationID" = 74;
```

6. LaGuardia Airport

```
-- LocationId = 74
SELECT index, "LocationID"
FROM taxi_zone
WHERE taxi_zone."Zone" = 'East Harlem North';

-- DOLocationId = 138
SELECT "DOLocationID", tip_amount
FROM tripdata
WHERE (lpep_pickup_datetime BETWEEN  '2025-11-01' AND '2025-11-30') AND
	"PULocationID" = 74
ORDER BY tip_amount DESC 
LIMIT 5;

SELECT "Zone" FROM taxi_zone WHERE "LocationID" = 138;

```