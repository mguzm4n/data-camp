## All answers

- 1.- 134.5 (opción 2)
- 2.- No rendered used, so string will be printed literally.
options.taxi - tripdata - .. (sin rendered - opcion 1)
- 3.- I did it by hand, sorry. The sum is: 24,648,499.

01- 6405008 
02- 6299354
03- 3007292
04- 237993
05- 348371
06- 549760
07- 800412
08- 1007284
09- 1341012
10- 1681131
11- 1508985
12- 1461897

- 4. Here, I used BigQuery console directly:


```
SELECT  count(*)
FROM `sublime-seat-484418-h6.zoomcamp.green_tripdata` as green_td
WHERE STARTS_WITH(green_td.filename, "green_tripdata_2020")
```

It should output: 1734051.
Ans: 1,734,051.

- 5. 1925152

- 6.

Add a timezone property set to America/New_York in the Schedule trigger configuration