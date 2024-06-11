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
    print(cleaned_card_df.info())
    print(cleaned_card_df.describe())
    print(cleaned_card_df.head(100))

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

    store_number_endpoint ='https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}'
      # Get the store number
    try:
        store_number_df = extractor.retrieve_stores_data(store_number_endpoint, headers, number_of_stores)
        print("Extracted Store Data:")
        print(store_number_df)
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")








