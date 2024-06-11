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
    
    def called_clean_store_data(self, df):
        #df = df.dropna(how='all')
        df = df.dropna(subset=['address','longitude','store_type', 'country_code', 'opening_date', 'continent',])
        # Fix continent names
        df['continent'] = df['continent'].replace({'eeEurope': 'Europe', 'eeAmerica': 'America'})
        # Filter valid continents
        #df = df[df['continent']].isin(['Europe', 'America'])
        df = df[df['continent'].isin(['Europe', 'America'])]
        # Filter invalid country codes
        df = df[df['country_code'].apply(lambda x: isinstance(x, str) and len(x) == 2 and x.isupper())]
        # Filter valid longitude and latitude
        df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
        df = df.dropna(subset=['longitude'])
        df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
        df = df.dropna(subset=['latitude'])
        # Ensure lat is a float, fill NaN values with 0.0
        df['lat'] = pd.to_numeric(df['lat'], errors='coerce').fillna(0.0)
        # Remove store types and localities containing digits
        df = df[~df['store_type'].str.contains(r'\d', na=False)]
        df = df[~df['locality'].str.contains(r'\d', na=False)]

        df.reset_index(drop=True, inplace=True)

        #invalid_indices=[]
        #for idx, row in df.iterrows():
        #    continent= str(row['continent'])
        #    latitude = row['latitude']
        #    longitude = row['longitude']
        #    country_code = str(row['country_code'])
        #    store_type = str(row['store_type'])
        #    locality = str(row['locality'])
        #    if continent !='Europe' or continent !='America':
        #        if continent=='eeEurope':
        #            continent.str.replace('eeEurope', 'Europe')
        #        elif continent=='eeAmerica':
        #            continent.str.replace('eeAmerica', 'America')
        #        else:
        #            invalid_indices.append(idx)
        #    if len(country_code) > 2:
        #        invalid_indices.append(idx)
        #    if longitude is not float:
        #        invalid_indices.append(idx)
        #    if bool(re.search(r'\d', store_type)) == True:
        #        invalid_indices.append(idx)
            
        #    if bool(re.search(r'\d', locality)) == True:
        #        invalid_indices.append(idx)
            

        
        #invalid_indices = list(set(invalid_indices))
                      
        
        #df.drop(invalid_indices, inplace=True)
        # Reset index after cleaning
        #df.reset_index(drop=True, inplace=True)

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
    
