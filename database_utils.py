import boto3
import pandas
import numpy
import csv
import yaml
from sqlalchemy import URL, create_engine, MetaData
#from data_cleaning import DataCleaning
#from data_extraction import DataExtractor

class DatabaseConnector:
    def read_db_creds(self, file_path='db_creds.yaml'):
        """
        Reads the database credentials from a YAML file and returns them as a dictionary.
        
        Parameters:
        file_path (str): The path to the YAML file containing the database credentials.
        
        Returns:
        dict: A dictionary containing the database credentials.
        """
        with open(file_path, 'r') as file:
            creds = yaml.safe_load(file)
        return creds
    def init_db_engine(self):
        """
        Initializes and returns a SQLAlchemy database engine using credentials from read_db_creds.
        
        Returns:
        sqlalchemy.engine.Engine: An SQLAlchemy engine instance connected to the database.
        """
        creds = self.read_db_creds()
        engine_str = f"postgresql://{creds['RDS_USER']}:{creds['RDS_PASSWORD']}@{creds['RDS_HOST']}:{creds['RDS_PORT']}/{creds['RDS_DATABASE']}"
        engine = create_engine(engine_str)
        return engine 
    
    def list_db_tables(self):
        """
        Lists all the tables in the database.
        
        Returns:
        list: A list of table names in the database.
        """
        engine = self.init_db_engine()
        meta = MetaData()
        meta.reflect(bind=engine)
        return meta.tables.keys()
    
    def upload_to_db(self, df, table_name):
        """
        Uploads a Pandas DataFrame to a specified table in the database.
        
        Parameters:
        df (pandas.DataFrame): The DataFrame to upload.
        table_name (str): The name of the table to upload the data to.
        """
        engine = self.init_db_engine()
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Data uploaded to {table_name} table successfully.")


# Testing the read_db_creds method
#if __name__ == "__main__":
#    connector = DatabaseConnector()
#    creds = connector.read_db_creds()
#    print("Database Credentials:", creds)

#    engine = connector.init_db_engine()
#    print("Database Engine", engine)

