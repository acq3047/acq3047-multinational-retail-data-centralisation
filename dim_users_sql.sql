/*
 Cast the coulms of dim_users to correct the data types
 */
-- Assign the maximum lenght of the country_code
-- Ensure the columns are of type TEXT 
ALTER TABLE dim_users
ALTER COLUMN country_code TYPE TEXT USING country_code::TEXT;
-- Find the maximum length of country code
SELECT MAX(LENGTH(country_code)) as max_length_country_code
FROM dim_users;
-- Fix the country_code data type
ALTER TABLE dim_users
ALTER COLUMN country_code TYPE VARCHAR(3);
-- Fix the first name data type
ALTER TABLE dim_users
ALTER COLUMN first_name TYPE VARCHAR(255);
-- Fix the last name data type
Alter TABLE dim_users
ALTER COLUMN last_name TYPE VARCHAR(255);
-- Fix the date of birth data type
ALTER TABLE dim_users
ALTER COLUMN date_of_birth TYPE DATE USING date_of_birth::DATE;
-- Fix the user_uuid data type
ALTER TABLE dim_users
ALTER COLUMN user_uuid TYPE UUID USING user_uuid::UUID;
-- Fix the join date data type
ALTER TABLE dim_users
ALTER COLUMN join_date TYPE DATE USING join_date::DATE;
-- Create the primary keys of the dim_users
--ALTER TABLE dim_users
--DROP CONSTRAINT pk_dim_users
ALTER TABLE dim_users
ADD primary key (user_uuid);
SELECT conname,
    contype
FROM pg_constraint
WHERE conrelid = 'dim_users'::regclass;