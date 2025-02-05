import pandas as pd
import sqlite3
import logging

# Configure logging
# %(asctime)s inserts a timestamp

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Read data from the CSV file ('train.csv')
# and return it as a DataFrame using pandas
def extract_data(file_path: str) -> pd.DataFrame:
    """Extract data from a CSV file."""
    logging.info("Extracting data from %s", file_path)
    try:
        df = pd.read_csv(file_path)
        logging.info("Data shape: %s", df.shape)
        return df
    except Exception as e:
        logging.error("Error reading CSV file: %s", e)
        raise

# Cleans and transform the dataset
# Fills missing values ('Age','Embarked')
# Drop Cabin column
# Create 'Family Size' column
# Convert to category types ('Sex','Embarked')

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and transform the Titanic dataset."""
    logging.info("Starting data transformation")

    # Fill missing values
    df['Age'].fillna(df['Age'].median(), inplace=True)
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
    
    # Drop the Cabin column due to 687 missing values
    df.drop('Cabin', axis=1, inplace=True)
    
    # Create Family Size feature
    df['Family Size'] = df['SibSp'] + df['Parch'] + 1

    # Convert columns to category types
    df['Sex'] = df['Sex'].astype('category')
    df['Embarked'] = df['Embarked'].astype('category')

    missing_values = df.isnull().sum().sum()
    logging.info("Total missing values after cleaning: %d", missing_values)
    return df


# Loads the transformed data into SQLite database
def load_data(df: pd.DataFrame, db_path: str, table_name: str) -> None:
    """Load the transformed data into a SQLite database."""
    logging.info("Loading data into database: %s, table: %s", db_path, table_name)
    try:
        conn = sqlite3.connect(db_path)
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        conn.close()
        logging.info("Data loaded successfully")
    except Exception as e:
        logging.error("Error loading data into database: %s", e)
        raise

def main():
    # Define file paths
    input_file = 'train.csv'     # Path of the CSV file that contains the data provided by Kaggle
    db_path = 'titanic.db'       # Path of the SQLite database file to store the cleaned data
    table_name = 'train_cleaned' # Name of the table within the SQLite database file 

    # Execute the ETL pipeline
    df = extract_data(input_file) # extract_data() function is called to read data from CSV file and return it as a DataFrame
    df_transformed = transform_data(df) # transform_data() function takes the DataFrame produced by extract_data(input_file) and cleans and transform the dataset
    load_data(df_transformed, db_path, table_name) # load_data() function loads the transformed data into SQLite database
    logging.info("ETL process completed successfully")

if __name__ == '__main__':
    main()
