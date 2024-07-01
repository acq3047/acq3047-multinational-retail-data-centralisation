# Multinational Retail Data Centralisation
# Table of contents
1. [Description](#description)
2. [Milestone 1: Set up the environment](#milestone-1-set-up-the-environment)
    - [Usage instructions](#usage-instructions)
3. [Milestone 2: Extract and clean data from the data sources](#milestone-2-extract-and-clean-data-from-the-data-sources)
    - [Task 1: Initialise the three project Classes](#task-1-initialise-the-three-project-classes)
    - [Task 2: Extract and clean the user data](#task-2-extract-and-clean-the-user-data)
    - [Task 3: Extracting users and cleaning card data](#task-3-extracting-users-and-cleaning-card-data)
    - [Task 4: Extract and clean the details of each store](#task-4-extract-and-clean-the-details-of-each-store)
    - [Task 5: Extract and clean the product data](#task-5-extract-and-clean-the-product-data)
    - [Task 8: Retrieve and clean the date events data](#task-8-retrieve-and-clean-the-date-events-data)
4. [Milestone 3: Create the database schema](#milestone-3-create-the-database-schema)
    -[Task 1: Cast the columns of the orders_table to the correct data types](#task-1-cast-the-columns-of-the-orders_table-to-the-correct-data-types)
    -[Task 2: Cast the columns of the dim_users to the correct data types](#task-2-cast-the-columns-of-the-dim_users-to-the-correct-data-types)
    -[Task 3: Update the dim_store_details table](#task-3-update-the-dim_store_details-table)
    -[Task 4: Make changes to the dim_products table for the delivery team and update the data types](#task-4-make-changes-to-the-dim_products-table-for-the-delivery-team-and-update-the-data-types)
    -[Task 5: Update the dim_date_times table](#task-5-update-the-dim_date_times-table)
    -[Task 6: Update the dim_card_details table](#task-6-update-the-dim_card_details-table)
    -[Task 7: Create the prymary keys in the dimension tables](#task-7-create-the-prymary-keys-in-the-dimension-tables)
    -[Task 8: Add the foreign keys to the orders table](#task-8-add-the-foreign-keys-to-the-orders-table)
5. [Milestone 4: Querying the data](#milestone-4-querying-the-data)
    - [Task 1: How many stores does the business have and in which countries?](#task-1-how-many-stores-the-company-have-and-in-which-countries)
    - [Task 2: Which locations currently have the most stores?](#task-2-which-locations-currently-have-the-most)
    - [Task 3: Which months produced the largest amount of sales?](#task-3-which-months-produced-the-largest-amount-of-sales)
    - [Task 4: How many of sales are coming from online?](#task-4-how-many-of-sales-are-coming-from-online)
    - [Task 5: What percentage of sales comes from each store type?](#task-5-what-percentage-of-sales-comes-from-each-store-type)
    - [Task 6: Which month in each year produced the highest cost sales](#task-6-which-month-in-each-year-produced-the-highest-cost-sales)
    - [Task 7: What is your staff headcount?](#task-7-what-is-your-staff-headcount)
    - [Task 8: Which store type is selling the most?](#task-8-which-store-type-is-selling-the-most)
    - [Task 9: How quickly is the company making sales?](#task-9-how-quickly-is-the-company-making-sales)
6. [Document your project](#document-your-project)
7. [License](#license)


## Description

This project will operate as a recreation of a Multinational Retail Data Centralisation in which their sales data is spread across many different data sources making it not easily accessible or analysable by current members of the team.

The main target of this project is based on the extraction and cleaning the data from the data sources and the creation of a database in which store the extracted data.

## Milestone 1: Set up the environment

The initial phase of the project entails establishing the project repository.

At the time of creating the repository, we decided to follow the following proccedure:

![All Text](https://github.com/acq3047/hangman272/blob/main/Set_up_the_environment.gif)

- Click on “Install Github App “ button on right panel on the Hangman project module of the AI Core portal. A new Github page will appear.
- Select the account on which you want to use for your AiCore projects
- On the next page, select the “All repositories“ checkbox.
- Click “Install & authorize“. You may be prompted to enter your password.
- Once the authorization and installation is complete, you can clone the created repository in the pyhton code editor that you have decided to use.

```python
git clone https://github.com/acq3047/hangman272.git
```

Once we have clone the repository, we proceeded to set up a new database on **pgadmin4** called **sales_data** which will store  all the company information once you extract it for the various data sources.

### Usage instructions
In this section, we will outline the necessary instructions for running the project, focusing on the specific version of Python required in this project.

***Python version***
- Python version: Python 3.7 or higher

***SQL version**
- PostgreSQL
- pgADMIN 4
***Packages***
- boto3
- yaml
- sqlalchemy
- requests
- pandas
- re
- tabula - This package requires a ***Java 8+** bing already installed in your laptopt not raise an error

## Milestone 2: Extract and clean data from the data sources

This milestone, will consists on the extraction of the data from multitude of data sources and the corresponding cleaning of the data extracted prior storing in the database created previously.

### Task 1: Initialise the three project Classes

In this task you will be defining the scripts and Classes you will use to extract and clean the data from multiple data sources.
The Class methods won't be defined in this step yet they will be defined when required in the subsequent tasks.

1. Step 1:

Create a new Python script named data_extraction.py and within it, create a class named DataExtractor.
This class will work as a utility class, in it you will be creating methods that help extract data from different data sources.
The methods contained will be fit to extract data from a particular data source, these sources will include CSV files, an API and an S3 bucket.

```python
class DataExtractor:
    """
    This class will work as a utility class, in it you will be creating methods
    that help extract data from different data sources.
    The methods contained will be fit to extract data from a particular data source,
    these sources will include CSV files, an API and an S3 bucket.
    """
    def __init__(self, connector):
        self.connector = connector
```

2. Step 2:

Create another script named database_utils.py and within it, create a class DatabaseConnector which you will use to connect with and upload data to the database.

```python
class DatabaseConnector:
    """
    This class will work as a utility class, in it you will be creating methods
    that help extract data from different data sources.
    The methods contained will be fit to extract data from a particular data source,
    these sources will include CSV files, an API and an S3 bucket.
    """
    pass
```

3. Step 3:

Finally, create a script named data_cleaning.py this script will contain a class DataCleaning with methods to clean data from each of the data sources.

```python
class DataCleaning:
    """
    This class will contain methods to clean data from each of the data sources.
    """
    pass
```

### Task 2: Extract and clean the user data

The historical data of users is currently stored in an AWS database in the cloud.
You will now create methods in your DataExtractor and DatabaseConnector class which help extract the information from an AWS RDS database.

1. Step 1:

The first step consists on the creation of the **db_creds.yaml** containing the database credentials

```yaml
RDS_HOST: data-handling-project-readonly.cq2e8zno855e.eu-west-1.rds.amazonaws.com
RDS_PASSWORD: AiCore2022
RDS_USER: aicore_admin
RDS_DATABASE: postgres
RDS_PORT: 5432
```
Once you have create the ***yaml*** file, include it in the ***.gitignore*** file to not upload the database credentials to your public GitHub repository.

2. Step 2:

Create a method called **read_db_creds** this will read the credentials yaml file and return a dictionary of the credentials. To do it, you require to have the ***yaml*** package in your script.

```python
import yaml
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
```

3. Step 3:

Create a method called **init_db_engine** which will read the credentials from the return of read_db_creds and initialise and return an sqlalchemy database engine.

```python
import yaml
from sqlalchemy import URL, create_engine, MetaData
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
```

4. Step 4:

Using the engine from init_db_engine create a method list_db_tables to list all the tables in the database so you know which tables you can extract data from.

```python
import yaml
from sqlalchemy import URL, create_engine, MetaData
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
```

Then, develop a method inside your DataExtractor class to read the data from the RDS database.

```python
from sqlalchemy import Table, MetaData
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
```

5. Step 5

Develop a method called read_rds_table in your DataExtractor class which will extract the database table to a pandas DataFrame takng an instance of the **DatabaseConnector** class and the table name as an argument and return a pandas DataFrame.
Use your **list_db_tables** method to get the name of the table containing user data.
Use the **read_rds_table** method to extract the table containing user data and return a pandas DataFrame.

```python
from sqlalchemy import Table, MetaData
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
```
6. Step 6:

Create a method called **clean_user_data** in the **DataCleaning** class which will perform the cleaning of the user data.

You will need clean the user data, look out for NULL values, errors with dates, incorrectly typed values and rows filled with the wrong information.

```python
import pandas as pd
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
```

7. Step 7:

Now create a method in your **DatabaseConnector** class called **upload_to_db**. This method will take in a Pandas DataFrame and table name to upload to as an argument.

```python
import yaml
from sqlalchemy import URL, create_engine, MetaData
import pandas as pd
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
    
    def read_local_creds(self, local_file_path='local_creds.yaml'):
        """
        Reads the database credentials from a YAML file and returns them as a dictionary.
        
        Parameters:
        file_path (str): The path to the YAML file containing the database credentials.
        
        Returns:
        dict: A dictionary containing the database credentials.
        """
        with open(local_file_path, 'r') as f:
            local_creds = yaml.safe_load(f)
        return local_creds
    
    def init_local_engine(self):
        """
        Initializes and returns a SQLAlchemy database engine using credentials from read_local_creds.
        
        Returns:
        sqlalchemy.engine.Engine: An SQLAlchemy engine instance connected to the database.
        """
        local_creds = self.read_local_creds()
        local_engine_str = create_engine(f"{local_creds['DATABASE_TYPE']}+{local_creds['DBAPI']}://{local_creds['USER']}:{local_creds['PASSWORD']}@{local_creds['HOST']}:{local_creds['PORT']}/{local_creds['DATABASE']}")
        #local_engine = create_engine(local_engine_str)
        return local_engine_str
    
    def upload_to_db(self, df, table_name):
        """
        Uploads a Pandas DataFrame to a specified table in the database.
        
        Parameters:
        df (pandas.DataFrame): The DataFrame to upload.
        table_name (str): The name of the table to upload the data to.
        """
        
        # Database connection details
        #engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")

        engine = self.init_local_engine()
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Data uploaded to {table_name} table successfully.")
```
8. Step 8:

Once extracted and cleaned use the **upload_to_db method** to store the data in your **sales_data database** in a table named **dim_users**. To do it, we created another script called **test.py**.

```python
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
```

### Task 3: Extracting users and cleaning card data

In this task, we proceed to extract the users card details that are stored in a PDF document in an AWS S3 bucket.

1. Step 1:

Install the Python package **tabula-py** this will help you to extract data from a pdf document.

```python
pip install tabula-py
```

2. Step 2:

Create a method in your **DataExtractor** class called **retrieve_pdf_data**, which takes in a link as an argument and returns a pandas DataFrame.
Use the **tabula-py** Python package, imported with tabula to extract all pages from the pdf document and return the dataframe of the extracted data .

```python
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
```

3. Step 3:

Create a method called **clean_card_data** in your **DataCleaning** class to clean the data to remove any erroneous values, NULL values or errors with formatting.

```python
import pandas as pf
import re
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
```

4. Step 4:

Once cleaned, upload the table with your **upload_to_db** method to the database in a table called **dim_card_details**.

```python
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
```

### Task 4: Extract and clean the details of each store

The store data can be retrieved through the use of an API.
The API has two GET methods. One will return the number of stores in the business and the other to retrieve a store given a store number.
To connect to the API you will need to include the API key to connect to the API in the method header.
Create a dictionary to store the header details it will have a key x-api-key with the value yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX.
The two endpoints for the API are as follows:
- Retrieve a store: https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{store_number}
- Return the number of stores: https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores

1. Step 1:

Create a method in your **DataExtractor** class called **list_number_of_stores** which returns the number of stores to extract. It should take in the number of stores endpoint and header dictionary as an argument.

```python
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
```

2. Step 2:

Create another method **retrieve_stores_data** which will take the retrieve a store endpoint as an argument and extracts all the stores from the API saving them in a pandas DataFrame.

```python
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
```

3. Step 3:

Create a method in the **DataCleaning** class **called_clean_store_data** which cleans the data retrieve from the API and returns a pandas DataFrame.

```python
import re
import pandas as pd
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
        df = df.dropna(subset=['address','longitude','store_type', 'country_code', 'opening_date', 'continent'])
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
        return df
```

5. Step 5:

Upload your DataFrame to the database using the **upload_to_db** method storing it in the table **dim_store_details**.

```python
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
```

### Task 5: Extract and clean the product data

The information for each product the company currently sells is stored in CSV format in an S3 bucket on AWS.

1. Step1:

Create a method in **DataExtractor** called **extract_from_s3** which uses the boto3 package to download and extract the information returning a pandas DataFrame.

The S3 address for the products data is the following s3://data-handling-public/products.csv the method will take this address in as an argument and return the pandas DataFrame.

```python
import boto3
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
        """
        Downloads a CSV file from an S3 bucket and returns it as a pandas DataFrame.

        Parameters:
        s3_address (str): The S3 address of the CSV file (e.g., 's3://bucket-name/file.csv').

        Returns:
        pandas.DataFrame: The DataFrame containing the data from the CSV file.
        """
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
```

2. Step 2:

Create a method in the **DataCleaning** class called **convert_product_weights** this will take the products DataFrame as an argument and return the products DataFrame.
If you check the weight column in the DataFrame the weights all have different units.
Convert them all to a decimal value representing their weight in kg. Use a 1:1 ratio of ml to g as a rough estimate for the rows containing ml.
Develop the method to clean up the weight column and remove all excess characters then represent the weights as a float.

```python
import boto3
import pandas as pd
import numpy
import re

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
        df = df.dropna(subset=['address','longitude','store_type', 'country_code', 'opening_date', 'continent'])
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
        return df
    def convert_product_weights(self, df):
        df = df.dropna(subset=['weight'])

        """
        Convert the weights in the DataFrame to a consistent unit (kg).
        
        Parameters:
        df (pandas.DataFrame): The DataFrame containing product data with a 'weight' column.
        
        Returns:
        pandas.DataFrame: The DataFrame with the 'weight' column converted to kg as a float.
        """

        def convert_weight(weight):
            if 'kg' in weight:
                try:
                    weight = weight.replace('kg','').strip()
                    return float(weight)
                except ValueError:
                    return None
            elif 'g' in weight:
                try:
                    weight = weight.replace('g','').strip()
                    return float(weight)/1000 # Convert grams to kg
                except ValueError:
                    return None
            elif 'ml' in weight:
                try:
                    weight = weight.replace('ml','').strip()
                    return float(weight)/1000  # Assume ml is roughly equivalent to g, then convert to kg
                except ValueError:
                    return None
            elif 'l' in weight:
                 try:
                    weight = weight.replaace('l', '').strip()
                    return float(weight)  # Liters to kg (assuming 1L ~ 1kg for water-like substances)
                 except ValueError:
                     return None
        
        df['weight'] = df['weight'].apply(convert_weight)
        return df
```

3. Step 3:

Create another method called **clean_products_data** this method will clean the DataFrame of any additional erroneous values.

```python
import boto3
import pandas as pd
import numpy
import re

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
        df = df.dropna(subset=['address','longitude','store_type', 'country_code', 'opening_date', 'continent'])
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
        return df
    def convert_product_weights(self, df):
        df = df.dropna(subset=['weight'])

        """
        Convert the weights in the DataFrame to a consistent unit (kg).
        
        Parameters:
        df (pandas.DataFrame): The DataFrame containing product data with a 'weight' column.
        
        Returns:
        pandas.DataFrame: The DataFrame with the 'weight' column converted to kg as a float.
        """

        def convert_weight(weight):
            if 'kg' in weight:
                try:
                    weight = weight.replace('kg','').strip()
                    return float(weight)
                except ValueError:
                    return None
            elif 'g' in weight:
                try:
                    weight = weight.replace('g','').strip()
                    return float(weight)/1000 # Convert grams to kg
                except ValueError:
                    return None
            elif 'ml' in weight:
                try:
                    weight = weight.replace('ml','').strip()
                    return float(weight)/1000  # Assume ml is roughly equivalent to g, then convert to kg
                except ValueError:
                    return None
            elif 'l' in weight:
                 try:
                    weight = weight.replaace('l', '').strip()
                    return float(weight)  # Liters to kg (assuming 1L ~ 1kg for water-like substances)
                 except ValueError:
                     return None
        
        df['weight'] = df['weight'].apply(convert_weight)
        return df

    def clean_products_data(self, df):
        """
        Clean the products data by removing the None vues and fixing errors in the data of ech column.
        
        Parameters:
        df (pandas.DataFrame): The DataFrame containing user data to be cleaned.
        
        Returns:
        pandas.DataFrame: The cleaned DataFrame.
        """
        df = df.dropna(subset=['product_name','product_price','weight','category','EAN','date_added','uuid','removed','product_code'])
        # Fix product_price errors
        df = df[~df['product_price'].str.contains(r'[a-zA-Z]', na=False)]
        # Fix availability errors
        df = df[~df['removed'].str.contains(r'\d', na=False)]
        # Fix category errors 
        df = df[~df['category'].str.contains(r'\d', na=False)]
        return df
```

4. Step 4:

Once complete insert the data into the **sales_data** database using your **upload_to_db** method storing it in a table named **dim_products**.

```python
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
```

### Task 6: Retrieve and clean the orders table

This table which acts as the single source of truth for all orders the company has made in the past is stored in a database on AWS RDS.

1. Step 1:

Using the database table listing methods you created earlier **list_db_tables**, list all the tables in the database to get the name of the table containing all information about the product orders.

```python
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
```

2. Step 2:

Extract the orders data using the **read_rds_table** method you create earlier returning a pandas DataFrame.

```python
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
```

3. Step 3:

Create a method in **DataCleaning** called **clean_orders_data** which will clean the orders table data.
You should remove the columns, first_name, last_name and 1 to have the table in the correct form before uploading to the database.
You will see that the orders data contains column headers which are the same in other tables.
This table will act as the source of truth for your sales data and will be at the center of your star based database schema.

```pyhton
import boto3
import pandas as pd
import numpy
import re

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
        df = df.dropna(subset=['address','longitude','store_type', 'country_code', 'opening_date', 'continent'])
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
        return df
    def convert_product_weights(self, df):
        df = df.dropna(subset=['weight'])

        """
        Convert the weights in the DataFrame to a consistent unit (kg).
        
        Parameters:
        df (pandas.DataFrame): The DataFrame containing product data with a 'weight' column.
        
        Returns:
        pandas.DataFrame: The DataFrame with the 'weight' column converted to kg as a float.
        """

        def convert_weight(weight):
            if 'kg' in weight:
                try:
                    weight = weight.replace('kg','').strip()
                    return float(weight)
                except ValueError:
                    return None
            elif 'g' in weight:
                try:
                    weight = weight.replace('g','').strip()
                    return float(weight)/1000 # Convert grams to kg
                except ValueError:
                    return None
            elif 'ml' in weight:
                try:
                    weight = weight.replace('ml','').strip()
                    return float(weight)/1000  # Assume ml is roughly equivalent to g, then convert to kg
                except ValueError:
                    return None
            elif 'l' in weight:
                 try:
                    weight = weight.replaace('l', '').strip()
                    return float(weight)  # Liters to kg (assuming 1L ~ 1kg for water-like substances)
                 except ValueError:
                     return None
        
        df['weight'] = df['weight'].apply(convert_weight)
        return df
```

3. Step 3:

Create another method called **clean_products_data** this method will clean the DataFrame of any additional erroneous values.

```python
import boto3
import pandas as pd
import numpy
import re

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
        df = df.dropna(subset=['address','longitude','store_type', 'country_code', 'opening_date', 'continent'])
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
        return df
    def convert_product_weights(self, df):
        df = df.dropna(subset=['weight'])

        """
        Convert the weights in the DataFrame to a consistent unit (kg).
        
        Parameters:
        df (pandas.DataFrame): The DataFrame containing product data with a 'weight' column.
        
        Returns:
        pandas.DataFrame: The DataFrame with the 'weight' column converted to kg as a float.
        """

        def convert_weight(weight):
            if 'kg' in weight:
                try:
                    weight = weight.replace('kg','').strip()
                    return float(weight)
                except ValueError:
                    return None
            elif 'g' in weight:
                try:
                    weight = weight.replace('g','').strip()
                    return float(weight)/1000 # Convert grams to kg
                except ValueError:
                    return None
            elif 'ml' in weight:
                try:
                    weight = weight.replace('ml','').strip()
                    return float(weight)/1000  # Assume ml is roughly equivalent to g, then convert to kg
                except ValueError:
                    return None
            elif 'l' in weight:
                 try:
                    weight = weight.replaace('l', '').strip()
                    return float(weight)  # Liters to kg (assuming 1L ~ 1kg for water-like substances)
                 except ValueError:
                     return None
        
        df['weight'] = df['weight'].apply(convert_weight)
        return df

    def clean_products_data(self, df):
        """
        Clean the products data by removing the None vues and fixing errors in the data of ech column.
        
        Parameters:
        df (pandas.DataFrame): The DataFrame containing user data to be cleaned.
        
        Returns:
        pandas.DataFrame: The cleaned DataFrame.
        """
        df = df.dropna(subset=['product_name','product_price','weight','category','EAN','date_added','uuid','removed','product_code'])
        # Fix product_price errors
        df = df[~df['product_price'].str.contains(r'[a-zA-Z]', na=False)]
        # Fix availability errors
        df = df[~df['removed'].str.contains(r'\d', na=False)]
        # Fix category errors 
        df = df[~df['category'].str.contains(r'\d', na=False)]
        return df
    
    def clean_orders_data(self, df):
        """
        Clean the data of the orders table by removing the first name, last name and 1 columns
        to have the table in the correct form before uploading to the database.

        Parameters:
        df (pandas.DataFrame): The DataFrame containing user data to be cleaned.
        
        Returns:
        pandas.DataFrame: The cleaned DataFrame.
        """
        df.drop(columns = ['first_name', 'last_name', '1'], inplace = True)
        return df
```

4. Step 4

Once cleaned upload using the **upload_to_db** method and store in a table called **orders_table**.

```python
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
```

### Task 8: Retrieve and clean the date events data

The final source of data is a JSON file containing the details of when each sale happened, as well as related attributes.
The file is currently stored on S3 and can be found at the following link https://data-handling-public.s3.eu-west-1.amazonaws.com/date_details.json.

1. Step 1:

Extract the date details data from the **date_details.json** file.

```python
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
```

2. Step 2:

Clean the data to have the table in the correct form before uploading to the database.

```python
import boto3
import pandas as pd
import numpy
import csv
import re
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
        df = df.dropna(subset=['address','longitude','store_type', 'country_code', 'opening_date', 'continent'])
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
        return df
    def convert_product_weights(self, df):
        df = df.dropna(subset=['weight'])

        """
        Convert the weights in the DataFrame to a consistent unit (kg).
        
        Parameters:
        df (pandas.DataFrame): The DataFrame containing product data with a 'weight' column.
        
        Returns:
        pandas.DataFrame: The DataFrame with the 'weight' column converted to kg as a float.
        """

        def convert_weight(weight):
            #weight = str(weight).lower().strip()
            #weight = re.sub(r'[^\d.]+', '', weight)  # Remove all non-numeric characters except decimal point
            if 'kg' in weight:
                try:
                    weight = weight.replace('kg','').strip()
                    return float(weight)
                except ValueError:
                    return None
            elif 'g' in weight:
                try:
                    weight = weight.replace('g','').strip()
                    return float(weight)/1000 # Convert grams to kg
                except ValueError:
                    return None
            elif 'ml' in weight:
                try:
                    weight = weight.replace('ml','').strip()
                    return float(weight)/1000  # Assume ml is roughly equivalent to g, then convert to kg
                except ValueError:
                    return None
            elif 'l' in weight:
                 try:
                    weight = weight.replaace('l', '').strip()
                    return float(weight)  # Liters to kg (assuming 1L ~ 1kg for water-like substances)
                 except ValueError:
                     return None
        
        df['weight'] = df['weight'].apply(convert_weight)
        return df
    
    def clean_products_data(self, df):
        """
        Clean the products data by removing the None vues and fixing errors in the data of ech column.
        
        Parameters:
        df (pandas.DataFrame): The DataFrame containing user data to be cleaned.
        
        Returns:
        pandas.DataFrame: The cleaned DataFrame.
        """
        df = df.dropna(subset=['product_name','product_price','weight','category','EAN','date_added','uuid','removed','product_code'])
        # Fix product_price errors
        df = df[~df['product_price'].str.contains(r'[a-zA-Z]', na=False)]
        # Fix availability errors
        df = df[~df['removed'].str.contains(r'\d', na=False)]
        # Fix category errors 
        df = df[~df['category'].str.contains(r'\d', na=False)]
        return df
    
    def clean_orders_data(self, df):
        """
        Clean the data of the orders table by removing the first name, last name and 1 columns
        to have the table in the correct form before uploading to the database.

        Parameters:
        df (pandas.DataFrame): The DataFrame containing user data to be cleaned.
        
        Returns:
        pandas.DataFrame: The cleaned DataFrame.
        """
        df.drop(columns = ['first_name', 'last_name', '1'], inplace = True)
        return df
    
    def clean_date_data(self,df):
        """
        Clean the data of the date table in order of 
        having the table in the correct form before uploading to the database.

        Parameters:
        df (pandas.DataFrame): The DataFrame containing user data to be cleaned.
        
        Returns:
        pandas.DataFrame: The cleaned DataFrame.
        """
        # Drop all rows containing null values in the following columns
        df = df.dropna(subset = ['timestamp','month','year','day','time_period','date_uuid'])
        # Fix month errors
        df = df[~df['month'].str.contains(r'[a-zA-Z]', na=False)]
        # Fix year errors
        df = df[~df['year'].str.contains(r'[a-zA-Z]', na=False)]
        # Fix day errors
        df = df[~df['day'].str.contains(r'[a-zA-Z]', na=False)]
        # Fix time_period erors
        df = df[~df['time_period'].str.contains(r'\d', na=False)]
        return df
```

3. Step 3:

Once the data is cleaned, upload the data to the database naming the table **dim_date_times**.

```python
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
```
## Milestone 3: Create the database schema

In this milestone, we proceed to develop the star-based schema of the database, ensuring that the columns are of the correct data types.

### Task 1: Cast the columns of the orders_table to the correct data types

In this task, we proceed to ensure that the columns of the **orders_table** is in the correct data type as shown in the following image along with identify the maximum length of the values with the ***?*** in the **VARCHAR** data type.

![alt text](https://github.com/acq3047/acq3047-multinational-retail-data-centralisation/blob/main/orders_table_sql.png)

```sql
-- The ? in VARCHAR should be replaced with an integer representing the maximum length of the values in that column. 
-- Find the maximum length of 'card_number'
-- Ensure the columns are of type TEXT
ALTER TABLE orders_table
ALTER COLUMN card_number TYPE TEXT USING card_number::TEXT;
ALTER TABLE orders_table
ALTER COLUMN store_code TYPE TEXT USING store_code::TEXT;
ALTER TABLE orders_table
ALTER COLUMN product_code TYPE TEXT USING product_code::TEXT;
-- Find the maximum lengths
SELECT MAX(LENGTH(card_number)) AS max_length_card_number
FROM orders_table;
SELECT MAX(LENGTH(store_code)) AS max_length_store_code
FROM orders_table;
SELECT MAX(LENGTH(product_code)) AS max_length_product_code
FROM orders_table;
-- Alter the 'card_number' column to VARCHAR with the appropriate length
ALTER TABLE orders_table
ALTER COLUMN card_number TYPE VARCHAR(19);
-- Alter the 'store_code' column to VARCHAR with the appropriate length
ALTER TABLE orders_table
Alter COLUMN store_code TYPE VARCHAR(12);
-- Alter the 'product_code' column to VARCHAR with the appropriate length
ALTER TABLE orders_table
ALTER COLUMN product_code TYPE VARCHAR(11);
-- Alter the 'date_uuid' column to UUID
ALTER TABLE orders_table
ALTER COLUMN date_uuid TYPE UUID USING date_uuid::UUID;
-- Alter the 'user_uuid' column to UUID
ALTER TABLE orders_table
ALTER COLUMN user_uuid TYPE UUID USING user_uuid::UUID;
-- Alter the 'product_quantity' column to SMALLINT
ALTER TABLE orders_table
ALTER COLUMN product_quantity TYPE SMALLINT;
```
### Task 2: Cast the columns of the dim_users to the correct data types

In this task, we proceed to ensure that the columns of the **dim_users** is in the correct data type as shown in the following image along with identify the maximum length of the values with the ***?*** in the **VARCHAR** data type.

![alt text](https://github.com/acq3047/acq3047-multinational-retail-data-centralisation/blob/main/dim_users_data_type.png)

```sql
-- Assign the maximum lenght of the country_code
-- Ensure the columns are of type TEXT 
ALTER TABLE dim_users
ALTER COLUMN country_code TYPE TEXT USING country_code::TEXT;
-- Find the maximum length of country code
SELECT MAX(LENGTH(country_code)) as max_length_country_code
FROM dim_users;
-- Fix the country_code data type
ALTER TABLE dim_users
ALTER COLUMN country_code TYPE VARCHAR(2);
-- Fix the first name data type
ALTER TABLE dim_users
ALTER COLUMN first_name TYPE VARCHAR(255);
-- Fix the last name data type
Alter TABLE dim_users
ALTER COLUMN last_name TYPE VARCHAR(255);
-- Fix the date of birth data type
ALTER TABLE dim_users
ALTER COLUMN date_of_birth TYPE DATE USING date_of_birth::DATE;
-- Fix the user_uuid data type
ALTER TABLE dim_users
ALTER COLUMN user_uuid TYPE UUID USING user_uuid::UUID;
-- Fix the join date data type
ALTER TABLE dim_users
ALTER COLUMN join_date TYPE DATE USING join_date::DATE;
```
### Task 3: Update the dim_store_details table

In this task, we proceed to ensure that the columns of the **dim_store_details** is in the correct data type as shown in the following image along with identify the maximum length of the values with the ***?*** in the **VARCHAR** data type.

![alt type](https://github.com/acq3047/acq3047-multinational-retail-data-centralisation/blob/main/dim_store_details_data_types.png)

```sql
-- Fix the longitude data type
ALTER TABLE dim_store_details
ALTER COLUMN longitude TYPE FLOAT USING longitude::FLOAT;
-- Fix the locality data type
ALTER TABLE dim_store_details
ALTER COLUMN locality TYPE VARCHAR(255);
-- Fix the store code data type
SELECT MAX(LENGTH(store_code)) AS max_length_store_code
FROM dim_store_details;
ALTER TABLE dim_store_details
ALTER COLUMN store_code TYPE VARCHAR(12);
-- Fix the staff numbers data type
ALTER TABLE dim_store_details
ALTER COLUMN staff_numbers TYPE SMALLINT USING staff_numbers::SMALLINT;
-- Fix the opening date data type
ALTER TABLE dim_store_details
ALTER COLUMN opening_date TYPE DATE USING opening_date::DATE;
-- Fix the store type data type
ALTER TABLE dim_store_details
ALTER COLUMN store_type TYPE VARCHAR(255);
-- Fix the latitude data type
ALTER TABLE dim_store_details
ALTER COLUMN latitude TYPE FLOAT USING latitude::FLOAT;
-- Fix the country code data type
SELECT MAX(LENGTH(country_code)) AS max_length_country_code
FROM dim_store_details;
ALTER TABLE dim_store_details
ALTER COLUMN country_code TYPE VARCHAR(2);
-- Fix the continent data type
ALTER TABLE dim_store_details
ALTER COLUMN continent TYPE VARCHAR(255);
```
### Task 4: Make changes to the dim_products table for the delivery team and update the data types

In this task, we will need to do some work on the **dim_products** products table before casting the data types correctly.
The product_price column has a ***£*** character which you need to remove using SQL.
The team that handles the deliveries would like a new human-readable column added for the weight so they can quickly make decisions on delivery weights.
Add a new column weight_class which will contain human-readable values based on the weight range of the product.
After all the columns are created and cleaned, change the data types of the products table.
You will want to rename the removed column to still_available before changing its data type.


![alt text](https://github.com/acq3047/acq3047-multinational-retail-data-centralisation/blob/main/dim_products_data_types.png)
![alt text](https://github.com/acq3047/acq3047-multinational-retail-data-centralisation/blob/main/dim_products_dtypes.png)

```sql
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
```
### Task 5: Update the dim_date_times table

In this task, we proceed to ensure that the columns of the **dim_date_times** is in the correct data type as shown in the following image along with identify the maximum length of the values with the ***?*** in the **VARCHAR** data type.

![alt text](https://github.com/acq3047/acq3047-multinational-retail-data-centralisation/blob/main/dim_date_times_table.png)

```sql
-- Fix the month data type
SELECT MAX(LENGTH(month)) AS max_length_month
FROM dim_date_times;
ALTER TABLE dim_date_times
ALTER COLUMN month TYPE VARCHAR(2);
-- Fix the year data type
SELECT MAX(LENGTH(year)) AS max_length_year
FROM dim_date_times;
ALTER TABLE dim_date_times
ALTER COLUMN year TYPE VARCHAR(4);
-- Fix the day data type
SELECT MAX(LENGTH(day)) AS max_length_day
FROM dim_date_times;
ALTER TABLE dim_date_times
ALTER COLUMN day TYPE VARCHAR(2);
-- Fix the time period data type
SELECT MAX(LENGTH(time_period)) AS max_length_time_period
FROM dim_date_times;
ALTER TABLE dim_date_times
ALTER COLUMN time_period TYPE VARCHAR(10);
-- Fix the date_uuid period data type
ALTER TABLE dim_date_times
ALTER COLUMN date_uuid TYPE UUID USING date_uuid::UUID;
```
### Task 6: Update the dim_card_details table

In this task, we proceed to ensure that the columns of the **dim_card_details** is in the correct data type as shown in the following image along with identify the maximum length of the values with the ***?*** in the **VARCHAR** data type.

![alt text](https://github.com/acq3047/acq3047-multinational-retail-data-centralisation/blob/main/dim_card_details_table.png)

```sql
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
```
### Task 7: Create the prymary keys in the dimension tables

Now that the tables have the appropriate data types we can begin adding the primary keys to each of the tables prefixed with dim.
Each table will serve the **orders_table** which will be the single source of truth for our orders.
Check the column header of the orders_table you will see all but one of the columns exist in one of our tables prefixed with dim.
We need to update the columns in the dim tables with a primary key that matches the same column in the orders_table.
Using SQL, update the respective columns as primary key columns.

```sql
ALTER TABLE dim_date_times
ADD PRIMARY KEY (date_uuid);

ALTER TABLE dim_users
ADD PRIMARY KEY (user_uuid);

ALTER TABLE dim_card_details
ADD PRIMARY KEY (card_number);

ALTER TABLE dim_store_details
ADD PRIMARY KEY (store_code);

ALTER TABLE dim_products
ADD PRIMARY KEY (product_code);
```
### Task 8: Add the foreign keys to the orders table

With the primary keys created in the tables prefixed with dim we can now create the foreign keys in the **orders_table** to reference the primary keys in the other tables.
Use SQL to create those foreign key constraints that reference the primary keys of the other table.
This makes the star-based database schema complete.

```sql
ALTER TABLE orders_table
ADD CONSTRAINT fk_orders_date FOREIGN KEY (date_uuid)
REFERENCES dim_date_times (date_uuid);

ALTER TABLE orders_table
ADD CONSTRAINT fk_orders_user FOREIGN KEY (user_uuid)
REFERENCES dim_users (user_uuid);

ALTER TABLE orders_table
ADD CONSTRAINT fk_orders_card FOREIGN KEY (card_number)
REFERENCES dim_card_details (card_number);

ALTER TABLE orders_table
ADD CONSTRAINT fk_orders_store FOREIGN KEY (store_code)
REFERENCES dim_store_details (store_code);

ALTER TABLE orders_table
ADD CONSTRAINT fk_orders_product FOREIGN KEY (product_code)
REFERENCES dim_products (product_code);
```

## Milestone 4: Querying the data

In this task. you have to start querying the data to get up to date metrics in order to get a better understanding of the sales' company from the database using **SQL**.

### Task 1: How many stores does the business have and in which countries?
The Operations team would like to know which countries we currently operate in and which country now has the most stores. Perform a query on the database to get the information.

```sql
SELECT country_code as country,
    count(store_code) as total_no_stores
FROM dim_store_details
GROUP BY country_code
ORDER BY total_no_stores DESC;
```
### Task 2: Which locations currently have the most?

The business stakeholders would like to know which locations currently have the most stores.
They would like to close some stores before opening more in other locations.
Find out which locations have the most stores currently. 

```sql
SELECT locality,
    count(store_code) as total_no_stores
FROM dim_store_details
GROUP BY locality
ORDER BY total_no_stores DESC; 
```
### Task 3: Which months produced the largest amount of sales?

Query the database to find out which months have produced the most sales.

```sql
SELECT d.month as month,
    SUM(o.product_quantity) as total_sales,
    SUM(p.product_price * o.product_quantity) as price
FROM orders_table o
    JOIN dim_date_times d ON o.date_uuid = d.date_uuid
    JOIN dim_products p ON o.product_code = p.product_code
GROUP BY month
ORDER BY price DESC;
```
### Task 4: How many of sales are coming from online?

The company is looking to increase its online sales.
They want to know how many sales are happening online vs offline.
Calculate how many products were sold and the amount of sales made for online and offline purchases.

```sql
SELECT count(o.product_quantity) AS product_quantity_count,
    CASE
        WHEN s.store_type = 'Website' THEN 'Web'
        ELSE 'Offline'
    END AS location,
    --COUNT(s.store_type) as location,
    SUM(p.product_price * o.product_quantity) as price
FROM orders_table o
    JOIN dim_products p ON o.product_code = p.product_code
    JOIN dim_store_details s ON o.store_code = s.store_code
GROUP BY location
ORDER BY location;
```

### Task 5: What percentage of sales comes from each store type?

The sales team wants to know which of the different store types is generated the most revenue so they know where to focus.
Find out the total and percentage of sales coming from each of the different store types.

```sql
WITH total_sales_by_store_type AS (
    SELECT s.store_type,
        SUM(p.product_price * o.product_quantity) AS total_sales
    FROM orders_table o
        JOIN dim_products p ON o.product_code = p.product_code
        JOIN dim_store_details s ON o.store_code = s.store_code
    GROUP BY s.store_type
),
total_sales_all AS (
    SELECT SUM(total_sales) AS grand_total_sales
    FROM total_sales_by_store_type
)
SELECT ts.store_type,
    ts.total_sales,
    (ts.total_sales / ta.grand_total_sales * 100) AS percentage_total
FROM total_sales_by_store_type ts,
    total_sales_all ta
ORDER BY ts.total_sales DESC;
```
### Task 6: Which month in each year produced the highest cost sales

The company stakeholders want assurances that the company has been doing well recently.
Find which months in which years have had the most sales historically.

```sql
SELECT SUM(p.product_price * o.product_quantity) AS total_sales,
    d.year as year,
    d.month as month
FROM orders_table o
    JOIN dim_date_times d ON o.date_uuid = d.date_uuid
    JOIN dim_products p ON o.product_code = p.product_code
GROUP BY d.year,
    d.month
ORDER BY total_sales DESC
Limit 10;
```
### Task 7: What is your staff headcount?

The operations team would like to know the overall staff numbers in each location around the world. Perform a query to determine the staff numbers in each of the countries the company sells in.

```sql
SELECT SUM(s.staff_numbers) AS total_staff_numbers,
    s.country_code
FROM dim_store_details s
GROUP BY s.country_code
ORDER BY total_staff_numbers DESC;
```
### Task 8: Which store type is selling the most?

The sales team is looking to expand their territory in Germany. Determine which type of store is generating the most sales in Germany.

```sql
SELECT SUM(p.product_price * o.product_quantity) AS total_sales,
    s.store_type as store_type,
    s.country_code as country_code
FROM orders_table o
    JOIN dim_products p ON o.product_code = p.product_code
    JOIN dim_store_details s ON o.store_code = s.store_code
WHERE s.country_code = 'DE'
GROUP BY s.store_type,
    s.country_code
ORDER BY total_sales ASC;
```
### Task 9: How quickly is the company making sales?

Sales would like the get an accurate metric for how quickly the company is making sales.
Determine the average time taken between each sale grouped by year.

```sql
WITH sales_with_lead AS (
    SELECT o.date_uuid,
        MAKE_DATE(
            CAST(d.year AS INTEGER),
            CAST(d.month AS INTEGER),
            CAST(d.day AS INTEGER)
        ) AS sale_date,
        LEAD(
            MAKE_DATE(
                CAST(d.year AS INTEGER),
                CAST(d.month AS INTEGER),
                CAST(d.day AS INTEGER)
            )
        ) OVER (
            PARTITION BY CAST(d.year AS INTEGER)
            ORDER BY MAKE_DATE(
                    CAST(d.year AS INTEGER),
                    CAST(d.month AS INTEGER),
                    CAST(d.day AS INTEGER)
                )
        ) AS next_date,
        CAST(d.year AS INTEGER) AS year
    FROM orders_table o
        JOIN dim_date_times d ON o.date_uuid = d.date_uuid
),
time_diffs AS (
    SELECT year,
        AVG((next_date - sale_date)) AS avg_time_diff_seconds
    FROM sales_with_lead
    WHERE next_date IS NOT NULL
    GROUP BY year
)
SELECT year,
    json_build_object(
        'hours',
        FLOOR(avg_time_diff_seconds / 3600),
        'minutes',
        FLOOR((avg_time_diff_seconds % 3600) / 60),
        'seconds',
        FLOOR(avg_time_diff_seconds % 60),
        'milliseconds',
        ROUND(
            (
                avg_time_diff_seconds - FLOOR(avg_time_diff_seconds)
            ) * 1000
        )
    ) AS actual_time_taken
FROM time_diffs
ORDER BY year DESC;
```

## Document your project

In the subsequent section, we will address the procedure for updating your Readme file locally and subsequently pushing the modifications to your GitHub repository. It is essential to document your progress diligently following the completion of each milestone. This entails providing a comprehensive description of the milestones, outlining the completed tasks, and embedding the code developed for each task. Finally, you must stage and push the changes to your GitHub repository.

```python
git add README.md
git commit -m "Your commit message"
git push
```

## License

When this project's repository was initially established, it was deliberately left unlicensed. This decision allows users to utilize, adapt, and distribute the code without encountering any constraints or limitations.