/*
 Milestone 4: Queryng the data
 */
-- Task 1: How many stores does the company have and in which countries?
SELECT country_code as country,
    count(store_code) as total_no_stores
FROM dim_store_details
GROUP BY country_code
ORDER BY total_no_stores DESC;
-- Task 2: Which locations currently have the most stores?
SELECT locality,
    count(store_code) as total_no_stores
FROM dim_store_details
GROUP BY locality
ORDER BY total_no_stores DESC -- Task 3: Which months produced the largest amount of sales?
SELECT *
FROM dim_products
SELECT *
FROM orders_table
SELECT d.month as month,
    SUM(o.product_quantity) as total_sales,
    SUM(p.product_price * o.product_quantity) as price
FROM orders_table o
    JOIN dim_date_times d ON o.date_uuid = d.date_uuid
    JOIN dim_products p ON o.product_code = p.product_code
GROUP BY month
ORDER BY price DESC;
-- How many of sales are coming from online?
SELECT *
FROM dim_store_details
SELECT *
FROM orders_table
SELECT count(o.product_quantity) AS product_quantity_count,
    CASE
        WHEN s.store_type = 'Website' THEN 'Web'
        ELSE 'Offline'
    END AS location,
    --COUNT(s.store_type) as location,
    SUM(p.product_price * o.product_quantity) as price
FROM orders_table o
    JOIN dim_products p ON o.product_code = p.product_code
    JOIN dim_store_details s ON o.store_code = s.store_code
GROUP BY location
ORDER BY location;
-- Task 5: What percentage of sales comes from each store type?
WITH total_sales_by_store_type AS (
    SELECT s.store_type,
        SUM(p.product_price * o.product_quantity) AS total_sales
    FROM orders_table o
        JOIN dim_products p ON o.product_code = p.product_code
        JOIN dim_store_details s ON o.store_code = s.store_code
    GROUP BY s.store_type
),
total_sales_all AS (
    SELECT SUM(total_sales) AS grand_total_sales
    FROM total_sales_by_store_type
)
SELECT ts.store_type,
    ts.total_sales,
    (ts.total_sales / ta.grand_total_sales * 100) AS percentage_total
FROM total_sales_by_store_type ts,
    total_sales_all ta
ORDER BY ts.total_sales DESC;
-- Task 6: Which month in each year produced the highest cost sales
SELECT SUM(p.product_price * o.product_quantity) AS total_sales,
    d.year as year,
    d.month as month
FROM orders_table o
    JOIN dim_date_times d ON o.date_uuid = d.date_uuid
    JOIN dim_products p ON o.product_code = p.product_code
GROUP BY d.year,
    d.month
ORDER BY total_sales DESC
Limit 10;
-- Task 7: What is your staff headcount?
SELECT SUM(s.staff_numbers) AS total_staff_numbers,
    s.country_code
FROM dim_store_details s
GROUP BY s.country_code
ORDER BY total_staff_numbers DESC;
-- Task 8: Which store type is selling the most?
SELECT *
FROM orders_table
SELECT SUM(p.product_price * o.product_quantity) AS total_sales,
    s.store_type as store_type,
    s.country_code as country_code
FROM orders_table o
    JOIN dim_products p ON o.product_code = p.product_code
    JOIN dim_store_details s ON o.store_code = s.store_code
WHERE s.country_code = 'DE'
GROUP BY s.store_type,
    s.country_code
ORDER BY total_sales ASC;
-- Task 9: How quickly is the company making sales?
WITH sales_with_lead AS (
    SELECT o.date_uuid,
        MAKE_DATE(
            CAST(d.year AS INTEGER),
            CAST(d.month AS INTEGER),
            CAST(d.day AS INTEGER)
        ) AS sale_date,
        LEAD(
            MAKE_DATE(
                CAST(d.year AS INTEGER),
                CAST(d.month AS INTEGER),
                CAST(d.day AS INTEGER)
            )
        ) OVER (
            PARTITION BY CAST(d.year AS INTEGER)
            ORDER BY MAKE_DATE(
                    CAST(d.year AS INTEGER),
                    CAST(d.month AS INTEGER),
                    CAST(d.day AS INTEGER)
                )
        ) AS next_date,
        CAST(d.year AS INTEGER) AS year
    FROM orders_table o
        JOIN dim_date_times d ON o.date_uuid = d.date_uuid
),
time_diffs AS (
    SELECT year,
        AVG((next_date - sale_date)) AS avg_time_diff_seconds
    FROM sales_with_lead
    WHERE next_date IS NOT NULL
    GROUP BY year
)
SELECT year,
    json_build_object(
        'hours',
        FLOOR(avg_time_diff_seconds / 3600),
        'minutes',
        FLOOR((avg_time_diff_seconds % 3600) / 60),
        'seconds',
        FLOOR(avg_time_diff_seconds % 60),
        'milliseconds',
        ROUND(
            (
                avg_time_diff_seconds - FLOOR(avg_time_diff_seconds)
            ) * 1000
        )
    ) AS actual_time_taken
FROM time_diffs
ORDER BY year DESC;