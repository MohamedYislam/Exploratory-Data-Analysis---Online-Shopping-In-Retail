import pandas as pd
import numpy as np
from pandas.api.types import is_numeric_dtype
from scipy import stats


class DataTransformer:
    """
    A class for transforming data within a pandas DataFrame.
    """

    def __init__(self, data_frame: pd.DataFrame):
        """
        Initialize the DataTransformer with a pandas DataFrame.

        Args:
            data_frame (pd.DataFrame): The DataFrame to be transformed.
        """
        self.df = data_frame.copy()

    def convert_columns(self, columns, dtype, errors='coerce'):
        """
        Convert specified columns to the specified data type.

        Args:
            columns (list): List of columns to be converted.
            dtype (str or type): The data type to convert the columns to.
            errors (str, optional): How to handle errors ('raise', 'ignore', 'coerce'). Defaults to 'coerce'.

        Returns:
            pd.DataFrame: The DataFrame with converted columns.
        """
        for column in columns:
            try:
                if is_numeric_dtype(dtype):
                    self.df[column] = pd.to_numeric(self.df[column], errors=errors)
                else:
                    self.df[column] = self.df[column].astype(dtype)
            except KeyError:
                print(f"Column '{column}' does not exist in the DataFrame")
            except Exception as e:
                print(f"An error occurred while converting column '{column}': {e}")

        return self.df

    def impute_null(self, columns, method='mean'):
        """
        Impute missing values in the specified DataFrame columns using the specified method.

        Args:
            columns (list): List of columns to impute missing values for.
            method (str): The method to use for imputation ('mean', 'median', 'mode').

        Returns:
            pd.DataFrame: The DataFrame with imputed columns.
        """
        for column in columns:
            if column not in self.df.columns:
                print(f"Column '{column}' does not exist in the DataFrame")
                continue

            if method == 'mean':
                value = self.df[column].mean()
            elif method == 'median':
                value = self.df[column].median()
            elif method == 'mode':
                value = self.df[column].mode()[0]
            else:
                print(f"Method '{method}' is not recognized. Use 'mean', 'median', or 'mode'.")
                continue

            self.df[column] = self.df[column].fillna(value)
        
        return self.df

    def remove_null(self, columns):
        """
        Remove rows with null values in the specified columns.

        Args:
            columns (list): List of columns to check for null values.

        Returns:
            pd.DataFrame: The DataFrame with rows containing null values in the specified columns removed.
        """
        self.df = self.df.dropna(subset=columns)
        return self.df


    def transform_skewed_columns(self, columns, method='box-cox'):
        """
        Apply transformation to specified skewed columns to reduce skewness.

        Args:
            columns (list): List of columns to transform.
            method (str): The transformation method to use ('box-cox' or 'log').

        Returns:
            pd.DataFrame: The DataFrame with transformed columns.
        """
        for column in columns:
            if column not in self.df.columns:
                print(f"Column '{column}' does not exist in the DataFrame")
                continue

            if method == 'box-cox':
                # Apply Box-Cox transformation
                self.df[column] = self.df[column].apply(lambda x: np.log(x) if x <= 0 else x)
                self.df[column], _ = stats.boxcox(self.df[column].dropna())
            elif method == 'log':
                # Apply log transformation
                self.df[column] = self.df[column].apply(lambda x: np.log(x) if x > 0 else np.nan)
            else:
                print(f"Method '{method}' is not recognized. Use 'box-cox' or 'log'.")
                continue

        return self.df