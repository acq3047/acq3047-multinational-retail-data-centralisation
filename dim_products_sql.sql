/*
 Make changes to the dim_products
 */
--- The product_price column has a £ character which you need to remove using SQL.
UPDATE dim_products
SET product_price = REPLACE(product_price, '£', '');
--- Add a new column weight_class which will contain human-readable values based on the weight range of the product.
ALTER TABLE dim_products
ADD COLUMN weight_class VARCHAR;
UPDATE dim_products
SET weight_class = CASE
        WHEN weight < 2 THEN 'Light'
        WHEN weight >= 2
        AND weight < 40 THEN 'Mid_Sized'
        WHEN weight >= 40
        AND weight < 140 THEN 'Heavy'
        ELSE 'Truck_Required'
    END;
/*
 After all the columns are created and cleaned, change the data types of the products table.
 
 You will want to rename the removed column to still_available before changing its data type.
 
 Make the changes to the columns to cast them to the following data types:
 */
-- Fix the product price data type
ALTER TABLE dim_products
ALTER COLUMN product_price TYPE FLOAT USING product_price::FLOAT;
-- Fix the weight data type
ALTER TABLE dim_products
ALTER COLUMN weight TYPE FLOAT USING weight::FLOAT;
-- Fix the EAN data type
SELECT MAX(LENGTH("EAN")) AS max_length_EAN
FROM dim_products;
ALTER TABLE dim_products
ALTER COLUMN "EAN" TYPE VARCHAR(17);
-- Fix the product_code data type
SELECT MAX(LENGTH(product_code)) AS max_length_product_code
FROM dim_products;
ALTER TABLE dim_products
ALTER COLUMN product_code TYPE VARCHAR(11);
-- Fix the date_added data type
ALTER TABLE dim_products
ALTER COLUMN date_added TYPE DATE USING date_added::DATE;
-- Fix the uuid data type
ALTER TABLE dim_products
ALTER COLUMN uuid TYPE UUID USING uuid::UUID;
-- FIX the weight_class data type
SELECT MAX(LENGTH(weight_class)) AS max_length_weight_class
FROM dim_products;
ALTER TABLE dim_products
ALTER COLUMN weight_class TYPE VARCHAR(14);
-- Chnge the name of removed to still_available Fix the still_avaliable data type
ALTER TABLE dim_products
    RENAME removed TO still_available;
UPDATE dim_products
SET still_available = CASE
        WHEN still_available = 'Still_avaliable' THEN TRUE
        ELSE FALSE
    END;
ALTER TABLE dim_products
ALTER COLUMN still_available TYPE BOOLEAN USING still_available::BOOLEAN;
-- Create the primary keys of the dim_products
--ALTER TABLE dim_products
--DROP CONSTRAINT pk_dim_products
ALTER TABLE dim_products
ADD PRIMARY KEY (product_code);
SELECT conname,
    contype
FROM pg_constraint
WHERE conrelid = 'dim_products'::regclass;