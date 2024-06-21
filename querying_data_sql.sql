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
FROM dim_products
SELECT *
FROM orders_table
SELECT *
FROM dim_card_details --SELECT count(o.product_quantity) AS product_quantity_count,
    --    s.store_type as location,