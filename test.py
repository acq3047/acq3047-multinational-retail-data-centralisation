from database_utils import DatabaseConnector
from data_extraction import DataExtractor
from data_cleaning import DataCleaning
import requests

if __name__ == "__main__":
    connector = DatabaseConnector()
    extractor = DataExtractor(connector)
    cleaner = DataCleaning()

    # Extract user data
    user_df = extractor.read_rds_table('legacy_users')
    print("Extracted User Data:")
    print(user_df)

    # Clean user data
    cleaned_user_df = cleaner.clean_user_data(user_df)
    print("Cleaned User Data:")
    print(cleaned_user_df)

    # Upload cleaned data to the dim_users table
    print('Upload the dim_users table')
    connector.upload_to_db(cleaned_user_df, 'dim_users')

    # Extract the pdf file
    user_tabula = extractor.retrieve_pdf_data('https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf')
    print('Data extracted from the PDF')
    print(user_tabula)

    # Clean the pdf file
    cleaner = DataCleaning()
    cleaned_card_df = cleaner.clean_card_data(user_tabula)
    print(cleaned_card_df)
    #print(cleaned_card_df.info())
    #print(cleaned_card_df.describe())
    #print(cleaned_card_df.head(100))

    # Upload cleaned data to the dim_card_details table
    print('Upload the dim_card_details table')
    connector.upload_to_db(cleaned_card_df, 'dim_card_details')


     # API details
    api_key = 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'
    headers = {
        'x-api-key': api_key
    }
    number_stores_endpoint = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores'

    # Get number of stores
    try:
        number_of_stores = extractor.list_number_of_stores(number_stores_endpoint, headers)
        print(f"Number of stores: {number_of_stores}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


    store_number = '45'
    store_number_endpoint ='https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}'
      # Get the store number
    store_number =int(store_number)
    try:
        store_number_df = extractor.retrieve_stores_data(store_number_endpoint, headers, number_of_stores)
        print("Extracted Store Data:")
        print(store_number_df)
        print(store_number_df.info())
        print(store_number_df['continent'].value_counts())
        print(store_number_df['locality'].value_counts())
        print(store_number_df['staff_numbers'].value_counts())
        print(store_number_df['opening_date'].value_counts())
        print(store_number_df['store_type'].value_counts())
        
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    # Clean the API data
    clean_api = DataCleaning()
    clean_api_df = clean_api.called_clean_store_data(store_number_df)
    print(clean_api_df)
    print(clean_api_df.info())
    print(clean_api_df['continent'].value_counts())
    print(clean_api_df['locality'].value_counts())
    print(clean_api_df['staff_numbers'].value_counts())
    print(clean_api_df['opening_date'].value_counts())
    print(clean_api_df['store_type'].value_counts())

    # Upload cleaned store data to the dim_store_details table

    print('Upload the dim_store_details table')
    connector.upload_to_db(clean_api_df, 'dim_store_details')
    print('Uploaded successful')

    # Extract product data from S3
    s3_address = 's3://data-handling-public/products.csv'
    try:
        product_df = extractor.extract_from_s3(s3_address)
        print("Extracted Product Data:")
        print(product_df)
        print(product_df.head(10))
        print(product_df.keys())
        print(product_df['weight'].value_counts())
        print(product_df['product_price'].value_counts())
        print(product_df['date_added'].value_counts())
        print(product_df['removed'].value_counts())
        print(product_df['category'].value_counts())
        print(product_df['product_name'].value_counts())
        print(product_df['uuid'].value_counts())
        print(product_df['product_code'].value_counts())
        print(product_df['EAN'].value_counts())
        print(product_df.info())
    except Exception as e:
        print(f"An error occurred while extracting product data: {e}")
    
    # Convert product weights
    cleaned_product_df = cleaner.convert_product_weights(product_df)
    print("Cleaned Product Data with Converted Weights:")
    print(cleaned_product_df.head())
    print(cleaned_product_df['weight'])

    # Clean product data
    cleaned_product_data_df = cleaner.clean_products_data(cleaned_product_df)
    print('Cleaned product data')
    print(cleaned_product_data_df)
    print(cleaned_product_data_df.info())
    print(cleaned_product_data_df['product_price'].value_counts())

    # Upload cleaned product data to the  dim_products table

    print('Upload the dim_store_details table')
    connector.upload_to_db(cleaned_product_data_df, 'dim_products')
    print('Uploaded successful')

    # list all the tables in the database to get the name of the table containing all information about the product orders.

    print("Listing all tables in the database:")
    tables_lst = connector.list_db_tables()
    print(tables_lst)

    #Extract the orders data using the read_rds_table method you create earlier returning a pandas DataFrame

    print("Read the orders from the product table")
    orders_data = extractor.read_rds_table('orders_table')
    print(orders_data)
    print(orders_data.info())

    # Clean orders data

    print('Removing the first_name, last_name and 1 colums')
    clean_orders_data = cleaner.clean_orders_data(orders_data)
    print(clean_orders_data)
    print(clean_orders_data.info())

    # Upload and store in a table called orders_table

    print('Upload the orders_table')
    order_connect = connector.upload_to_db(clean_orders_data, 'orders_table')
    print('Uploaded successful')

    # Extract date details data from S3

    s3_json_address = 'https://data-handling-public.s3.eu-west-1.amazonaws.com/date_details.json'

    try:
        date_df = extractor.extract_json_from_s3(s3_json_address)
        print("Extracted Product Data:")
        print(date_df)
        print(date_df.head(10))
        print(date_df.keys())
        print(date_df.info())
        print(date_df['timestamp'].value_counts())
        print(date_df['month'].value_counts())
        print(date_df['year'].value_counts())
        print(date_df['day'].value_counts())
        print(date_df['time_period'].value_counts())
        print(date_df['date_uuid'].value_counts())
        
    except Exception as e:
        print(f"An error occurred while extracting product data: {e}")
    
    # Clean the date  table

    print('Cleaning the date data')
    clean_date_df = cleaner.clean_date_data(date_df)
    print(clean_date_df)
    print(clean_date_df.info())
    print(clean_date_df['month'].value_counts())
    print(clean_date_df['timestamp'].value_counts())
    print(clean_date_df['time_period'].value_counts())
    print('Database successfully clean')

    # Upload the data to the database naming the table dim_date_times.
    print('Upload the date data')
    date_connect = connector.upload_to_db(clean_date_df, 'dim_date_times')
    print('Uploaded successful')

    














        







