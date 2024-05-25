import pandas as pd
from sqlalchemy.engine import Engine

class DataExtractor:
    """
    A class for extracting data from various sources.
    """

    def __init__(self, engine: Engine):
        """
        Initialize the DataExtractor with a SQLAlchemy engine.

        Args:
            engine (sqlalchemy.engine.Engine): The SQLAlchemy engine to use for data extraction.
        """
        self.engine = engine

    # Task 3 Step 6
    def read_rds_table(self, table_name: str) -> pd.DataFrame:
        """
        Read a table from the RDS database and load it into a pandas DataFrame.

        Args:
            table_name (str): The name of the table to read from the database.

        Returns:
            pd.DataFrame: A DataFrame containing the table data.
        """
        query = f"SELECT * FROM {table_name}"
        with self.engine.connect() as connection:
            data_frame = pd.read_sql(query, connection)
        return data_frame

    # Task 3 Step 7
    def save_to_csv(self, data_frame: pd.DataFrame, file_path: str):
        """
        Save a pandas DataFrame to a CSV file.

        Args:
            data_frame (pd.DataFrame): The DataFrame to save.
            file_path (str): The file path to save the CSV file.
        """
        data_frame.to_csv(file_path, index=False)