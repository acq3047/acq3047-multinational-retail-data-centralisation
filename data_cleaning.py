import boto3
import pandas as pd
import numpy
import csv
#from data_extraction import DataExtractor
#from database_utils import DatabaseConnector

class DataCleaning:
    """
    This class will contain methods to clean data from each of the data sources.
    """
    def clean_user_data(self,df):
        """
        Cleans user data by handling NULL values, correcting date errors, fixing data types, 
        and removing rows with invalid information.
        
        Parameters:
        df (pandas.DataFrame): The DataFrame containing user data to be cleaned.
        
        Returns:
        pandas.DataFrame: The cleaned DataFrame.
        """
        # Handle NULL values
        df2 = df.dropna(how='all')  # Drop rows where all elements are NULL
        df2 = df2.dropna(subset=['user_uuid', 'join_date']) # Ensure crucial columns are not NULL

        # Fill remaining NULL values with appropriate defaults or drop
        df2['email_address'] = df2['email_address'].fillna('unknown@example.com')
        df2['phone_number'] = df2['phone_number'].fillna('000-000-0000')

        # Correct errors with dates

        df2['join_date']=pd.to_datetime(df['join_date'], errors='coerce')
        df2 = df2.dropna(subset=['join_date']) # Drop rows with invalid dates

        # Fix incorrectly typed values

        df2['user_uuid'] = df2['user_uuid'].astype(str)
        df2['email_address'] = df2['email_address'].astype(str)
        df2['phone_number'] = df2['phone_number'].astype(str)

        # Remove rows with invalid data
        # Assuming user_uuid should not be empty or default string 'unknown'
        #df = df[df['user_uuid'] != '']

        return df2


#if __name__ == "__main__":
#    # Assuming `user_df` is the DataFrame extracted using DataExtractor
#    connector = DatabaseConnector()
#    extractor = DataExtractor(connector)
#    user_table_name = 'legacy_users'
#    user_df = extractor.read_rds_table(connector, user_table_name)
#    
#    cleaner = DataCleaning()
#    cleaned_user_df = cleaner.clean_user_data(user_df)
#    print("Cleaned User DataFrame:")
#    print(cleaned_user_df)

    # Upload cleaned data to the dim_users table
#    connector.upload_to_db(cleaned_user_df, 'dim_users')
    
