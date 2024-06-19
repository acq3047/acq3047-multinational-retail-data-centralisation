/*
 Now update the date table with the correct types:
 */
-- Fix the month data type
SELECT MAX(LENGTH(month)) AS max_length_month
FROM dim_date_times;
ALTER TABLE dim_date_times
ALTER COLUMN month TYPE VARCHAR(2);
-- Fix the year data type
SELECT MAX(LENGTH(year)) AS max_length_year
FROM dim_date_times;
ALTER TABLE dim_date_times
ALTER COLUMN year TYPE VARCHAR(4);
-- Fix the day data type
SELECT MAX(LENGTH(day)) AS max_length_day
FROM dim_date_times;
ALTER TABLE dim_date_times
ALTER COLUMN day TYPE VARCHAR(2);
-- Fix the time period data type
SELECT MAX(LENGTH(time_period)) AS max_length_time_period
FROM dim_date_times;
ALTER TABLE dim_date_times
ALTER COLUMN time_period TYPE VARCHAR(10);
-- Fix the date_uuid period data type
ALTER TABLE dim_date_times
ALTER COLUMN date_uuid TYPE UUID USING date_uuid::UUID;
-- Create the primary keys of the dim_date_times
--ALTER TABLE dim_date_times
--DROP CONSTRAINT pk_dim_date_times
ALTER TABLE dim_date_times
ADD PRIMARY KEY (date_uuid);