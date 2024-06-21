/*
 Milestone 4: Queryng the data
 */
-- How many stores does the company have and in which countries?
SELECT country_code as country,
    count(store_code) as total_no_stores
FROM dim_store_details
GROUP BY country_code
ORDER BY total_no_stores DESC;