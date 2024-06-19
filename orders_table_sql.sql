/*
 Milestone 3: Create the database schema 
 */
-- The ? in VARCHAR should be replaced with an integer representing the maximum length of the values in that column. 
-- Find the maximum length of 'card_number'
-- Ensure the columns are of type TEXT
ALTER TABLE orders_table
ALTER COLUMN card_number TYPE TEXT USING card_number::TEXT;
ALTER TABLE orders_table
ALTER COLUMN store_code TYPE TEXT USING store_code::TEXT;
ALTER TABLE orders_table
ALTER COLUMN product_code TYPE TEXT USING product_code::TEXT;
-- Find the maximum lengths
SELECT MAX(LENGTH(card_number)) AS max_length_card_number
FROM orders_table;
SELECT MAX(LENGTH(store_code)) AS max_length_store_code
FROM orders_table;
SELECT MAX(LENGTH(product_code)) AS max_length_product_code
FROM orders_table;
-- Alter the 'card_number' column to VARCHAR with the appropriate length
ALTER TABLE orders_table
ALTER COLUMN card_number TYPE VARCHAR(19);
-- Alter the 'store_code' column to VARCHAR with the appropriate length
ALTER TABLE orders_table
Alter COLUMN store_code TYPE VARCHAR(12);
-- Alter the 'product_code' column to VARCHAR with the appropriate length
ALTER TABLE orders_table
ALTER COLUMN product_code TYPE VARCHAR(11);
-- Alter the 'date_uuid' column to UUID
ALTER TABLE orders_table
ALTER COLUMN date_uuid TYPE UUID USING date_uuid::UUID;
-- Alter the 'user_uuid' column to UUID
ALTER TABLE orders_table
ALTER COLUMN user_uuid TYPE UUID USING user_uuid::UUID;
-- Alter the 'product_quantity' column to SMALLINT
ALTER TABLE orders_table
ALTER COLUMN product_quantity TYPE SMALLINT;
SELECT *
FROM orders_table -- Add foreign keys
    -- Create foreign key constraint for date_uuid
    --ALTER TABLE orders_table
    --DROP CONSTRAINT fk_orders_date
ALTER TABLE orders_table
ADD CONSTRAINT fk_orders_date FOREIGN KEY (date_uuid) REFERENCES dim_date_times(date_uuid) -- Create foreign key constraint for user_uuid
ALTER TABLE orders_table
ADD CONSTRAINT fk_orders_user FOREIGN KEY (user_uuid) REFERENCES dim_users(user_uuid);
DROP CONSTRAINT -- ALTER TABLE orders_table DROP CONSTRAINT fk_orders_user;
-- Create foreign key constraint for card_number
ALTER TABLE orders_table
ADD CONSTRAINT fk_orders_card FOREIGN KEY (card_number) REFERENCES dim_card_details(card_number);
SELECT *
FROM orders_table
WHERE date_uuid NOT IN(
        SELECT
        FROM dim_date_times.date_uuid
        FROM dim_date_times
    );
​ ​
SELECT *
FROM orders_table
WHERE date_uuid NOT IN(
        SELECT ?
        FROM dim_date_times.date_uuid
        FROM dim_date_times
    );
SELECT *
FROM orders_table
WHERE card_number NOT IN(
        SELECT dim_card_details.card_number
        FROM dim_card_details
    );
SELECT *
FROM orders_table
WHERE date_uuid NOT IN(
        SELECT dim_date_times.date_uuid
        FROM dim_date_times
    );
-- Foreighn key of store data
ALTER TABLE orders_table
ADD CONSTRAINT fk_orders_store FOREIGN KEY (store_code) REFERENCES dim_store_details (store_code);