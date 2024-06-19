/*
 Now we need to update the dim_card_details table for the card details.
 */
-- Fix the card number data type
SELECT MAX(LENGTH(card_number)) AS max_length_card_number
FROM dim_card_details;
ALTER TABLE dim_card_details
ALTER COLUMN card_number TYPE VARCHAR(19);
-- Fix the expiry_date data type
SELECT MAX(LENGTH(expiry_date)) AS max_length_expiry_date
FROM dim_card_details;
ALTER TABLE dim_card_details
ALTER COLUMN expiry_date TYPE VARCHAR(5);
-- Fix the date_payment_confirmed data type
ALTER TABLE dim_card_details
ALTER COLUMN date_payment_confirmed TYPE DATE USING date_payment_confirmed::DATE;
-- Create the primary keys of the dim_card_details
--ALTER TABLE dim_card_details
--DROP CONSTRAINT pk_dim_card_details
ALTER TABLE dim_card_details
ADD PRIMARY KEY (card_number);