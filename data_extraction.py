import boto3
import pandas
import numpy
import csv
from database_utils import DatabaseConnector
from sqlalchemy import Table, MetaData
import pandas as pd

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
