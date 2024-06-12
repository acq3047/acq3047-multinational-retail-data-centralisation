import boto3
import numpy
import csv
from database_utils import DatabaseConnector
from sqlalchemy import Table, MetaData
import pandas as pd
import tabula
import requests

class DataExtractor:
    """
    This class will work as a utility class, in it you will be creating methods
    that help extract data from different data sources.
    The methods contained will be fit to extract data from a particular data source,
    these sources will include CSV files, an API and an S3 bucket.
    """
    def __init__(self, connector):
        self.connector = connector
    def read_data_from_table(self, table_name):
        """
        Reads data from a specified table in the database.
            
        Parameters:
        table_name (str): The name of the table from which to read data.
            
        Returns:
        list: A list of dictionaries representing rows of data from the table.
        """
        engine = self.connector.init_db_engine()
        metadata = MetaData()
        metadata.reflect(bind=engine)
        table = Table(table_name, metadata, autoload_with=engine)
        with engine.connect() as connection:
            query = table.select()
            result = connection.execute(query)
            data = [dict(row._mapping) for row in result]
        return data
    def read_rds_table(self, table_name):
        """
        Extracts a database table to a pandas DataFrame.

        Parameters:
        connector (DatabaseConnector): An instance of DatabaseConnector class.
        table_name (str): The name of the table to extract.

        Returns:
        pandas.DataFrame: A DataFrame containing the data from the specified table.
        """
        data = self.read_data_from_table(table_name)
        df = pd.DataFrame(data)
        return df
    
    def retrieve_pdf_data(self, link):
        dfs_tabula = tabula.read_pdf(link, pages='all', multiple_tables=True)
        dfs = pd.concat(dfs_tabula, ignore_index=True)
        return dfs
    
    def list_number_of_stores(self, endpoint, header):
        """
        Retrieves the number of stores from the API.

        Parameters:
        number_stores_endpoint (str): The API endpoint to get the number of stores.
        headers (dict): The headers containing the API key for authorization.

        Returns:
        int: The number of stores.
        """
        response = requests.get(endpoint, headers=header)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return data['number_stores']
        
    def retrieve_stores_data(self, store_details_endpoint, header, num_stores):
        """
        Retrieves data for all stores from the API and saves it in a pandas DataFrame.

        Parameters:
        store_details_endpoint (str): The API endpoint to get store details.
        headers (dict): The headers containing the API key for authorization.

        Returns:
        pandas.DataFrame: A DataFrame containing the data for all stores.
        """
        number_stores_endpoint = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores'
        num_stores = self.list_number_of_stores(number_stores_endpoint, header)
        retrieve_a_store_endpoint = 'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details'
        store_number = '451'
        store_number=int(store_number)

        #request_2= requests.get(f'{retrieve_a_store_endpoint}/{store_number}', headers=header)
        #data = request_2.json()
        #stores_data = []
        #stores_data.append(data)
        #stores_data_df = pd.DataFrame(stores_data)

        # Initialize an empty list to store data
        stores_data = []
        for store in range(num_stores):
            formatted_endpoint = store_details_endpoint.format(store_number=store)
            response_retrieve = requests.get(formatted_endpoint, headers=header)
            response_retrieve.raise_for_status()  # Raise an exception for HTTP errors
            data = response_retrieve.json()  
            #response_2=requests.get(f'{'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details'}/{'store_number'}', headers=self.header_dict)
            stores_data.append(data)
        stores_data_df = pd.DataFrame(stores_data)
        print(stores_data_df.head(5))
        return stores_data_df
    
    def extract_from_s3(self, s3_address):
        s3= boto3.client('s3')
        # Parse the S3 address
        bucket_name, key = self.parse_s3_address(s3_address)
        # Download the file from S3 to a temporary file
        temp_file = 'C:/Users/acq30/OneDrive/Documents/AI Core VsCode/acq3047-multinational-retail-data-centralisation/products.csv'
        s3.download_file(bucket_name, key, temp_file)
        # Read the temporary file into a pandas DataFrame
        df = pd.read_csv(temp_file)
        return df

    def parse_s3_address(self, s3_address):
        """
        Parses an S3 address into bucket name and key.

        Parameters:
        s3_address (str): The S3 address (e.g., 's3://bucket-name/file.csv').

        Returns:
        tuple: A tuple containing the bucket name and key.
        """
        if not s3_address.startswith('s3://'):
            raise ValueError("Invalid S3 address. It should start with 's3://'.")
        
        s3_parts = s3_address.replace('s3://', '').split('/', 1)
        bucket_name = s3_parts[0]
        key = s3_parts[1]
        
        return bucket_name, key




    

         


#if __name__ == "__main__":
#        connector = DatabaseConnector()
#        extractor = DataExtractor(connector)

        # List tables
#        tables = connector.list_db_tables()
#        print("Database Tables:", tables)

        # Read data from a table (example)
       # table_name = 'legacy_users'
       # data = extractor.read_data_from_table(table_name)
       # print(f"Data from table '{table_name}':")
       # for row in data:
       #     print(row)
        # Get the table name containing user data
#        user_table_name = 'legacy_users'

        # Extract the table containing user data to a pandas DataFrame
#        user_df = extractor.read_rds_table(connector, user_table_name)
#        print("User DataFrame:")
#        print(user_df)
#        print('keys', user_df.keys())

