import pandas as pd

class DataFrameInfo:
    def __init__(self, data_frame: pd.DataFrame):
        """
        Initialize the DataFrameInfo class with a DataFrame.

        Args:
            df (pd.DataFrame): The DataFrame to be analyzed.
        """
        self.df = data_frame

    def describe_columns(self):
        """
        Describe all columns in the DataFrame to check their data types and other summary statistics.

        Returns:
            pd.DataFrame: Summary statistics of the DataFrame.
        """
        description = self.df.describe(include='all')
        print("Column Description:\n", description)
        return description

    def statistics(self, column: str = None):
        """
        Extract median, standard deviation, and mean from the DataFrame or a specified column.

        Args:
            column (str, optional): The column name. Defaults to None.

        Returns:
            pd.Series or pd.DataFrame: Summary statistics of the column or the entire DataFrame.
        """
        if not column:  # If no argument was added, return the stats for the entire DataFrame
            stats = self.df.describe()
            print("Statistics for the entire DataFrame:\n", stats)
            return stats
        elif column in self.df.columns:  # If a particular column is specified, return the stats for it alone
            stats = self.df[column].describe()
            print(f"Statistics for column '{column}':\n", stats)
            return stats
        else:
            print("The column name you entered does not exist in the DataFrame")
            return None

    def count_distinct_values(self, column: str = None):
        """
        Count distinct values in the DataFrame or a specified categorical column.

        Args:
            column (str, optional): The column name. Defaults to None.

        Returns:
            int or dict: The count of distinct values in the column or a dictionary of counts for all categorical columns.
        """
        if not column:  # If no column is specified, return distinct counts for all categorical columns
            distinct_counts = {col: self.df[col].nunique() for col in self.df.select_dtypes(include=['category']).columns}
            print("Distinct values for all categorical columns:\n", distinct_counts)
            return distinct_counts
        elif column in self.df.columns:  # If a particular column is specified, return the distinct count for that column
            distinct_count = self.df[column].nunique()
            print(f"Distinct values in column '{column}': {distinct_count}")
            return distinct_count
        else:
            print("The column name you entered does not exist in the DataFrame")
            return None

    def print_shape(self):
        """
        Print the shape of the DataFrame.

        Returns:
            tuple: The shape of the DataFrame.
        """
        shape = self.df.shape
        print(f"Shape of the DataFrame: {shape}")
        return shape

    def null_percentage(self):
        """
        Generate a percentage count of NULL values in each column.

        Returns:
            pd.Series: A series with the percentage of NULL values for each column.
        """
        null_percent = self.df.isnull().mean() * 100
        return null_percent
