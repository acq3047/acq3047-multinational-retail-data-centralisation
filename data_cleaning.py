import boto3
import pandas as pd
import numpy
import csv
import re
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
    
    def clean_card_data(self,df):
        # Fix incorrectly typed values
        df = df.dropna(how='all')
        # Define regex patterns for validation
        card_number_pattern = re.compile(r'^\d{13,19}$')
        expiry_date_pattern = re.compile(r'^\d{2}/\d{2}$')
        date_format = '%Y-%m-%d'   

        # Ensure card_number is treated as a string
        df['card_number'] = df['card_number'].astype(str)

        def validate_card_number(card_number):
            return bool(card_number_pattern.match(card_number.replace(' ', '')))
        
        def validate_expiry_date(expiry_date):
            try:
                month, year = map(int, expiry_date.split('/'))
                return 1 <= month <= 12 and year >= 22  # Assuming '22' is the minimum valid year
            except:
                return False
        
        def validate_date(date_str):
            try:
                pd.to_datetime(date_str, format=date_format)
                return True
            except ValueError:
                return False

        # List to store indices of invalid rows
        invalid_indices = []
        
        for idx, row in df.iterrows():
            card_number = str(row['card_number']).replace(' ', '')
            expiry_date = row['expiry_date']
            date_payment_confirmed = row['date_payment_confirmed']
            
            if not validate_card_number(card_number) or not validate_expiry_date(expiry_date) or not validate_date(date_payment_confirmed):
                invalid_indices.append(idx)

        # Drop invalid rows
        df.drop(invalid_indices, inplace=True)

        # Reset index after cleaning
        df.reset_index(drop=True, inplace=True)
        

        return df
            








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
    
