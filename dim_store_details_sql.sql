/*
 Now we need to update the dim_store_details table for the card details.
 */
-- Fix the longitude data type
ALTER TABLE dim_store_details
ALTER COLUMN longitude TYPE FLOAT USING longitude::FLOAT;
-- Fix the locality data type
ALTER TABLE dim_store_details
ALTER COLUMN locality TYPE VARCHAR(255);
-- Fix the store code data type
SELECT MAX(LENGTH(store_code)) AS max_length_store_code
FROM dim_store_details;
ALTER TABLE dim_store_details
ALTER COLUMN store_code TYPE VARCHAR(11);
-- Fix the staff numbers data type
ALTER TABLE dim_store_details
ALTER COLUMN staff_numbers TYPE SMALLINT USING staff_numbers::SMALLINT;
-- Fix the opening date data type
ALTER TABLE dim_store_details
ALTER COLUMN opening_date TYPE DATE USING opening_date::DATE;
-- Fix the store type data type
ALTER TABLE dim_store_details
ALTER COLUMN store_type TYPE VARCHAR(255);
-- Fix the latitude data type
ALTER TABLE dim_store_details
ALTER COLUMN latitude TYPE FLOAT USING latitude::FLOAT;
-- Fix the country code data type
SELECT MAX(LENGTH(country_code)) AS max_length_country_code
FROM dim_store_details;
ALTER TABLE dim_store_details
ALTER COLUMN country_code TYPE VARCHAR(2);
-- Fix the continent data type
ALTER TABLE dim_store_details
ALTER COLUMN continent TYPE VARCHAR(255);
-- Create the primary keys of the dim_store_details
--ALTER TABLE dim_store_details
--DROP CONSTRAINT pk_dim_store_details
ALTER TABLE dim_store_details
ADD PRIMARY KEY (store_code);
SELECT *
FROM orders_table
SELECT conname,
    contype
FROM pg_constraint
WHERE conrelid = 'dim_store_details'::regclass;