import pandas as pd
from pandas.api.types import is_numeric_dtype

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
            columns (list or str): List of columns or a single column name to be converted.
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

    # Converting Columns and cleaning

    # def convert_columns(self):
    #     """
    #     Convert columns to the correct format for the DataFrame.
    #     """
    #     # Convert 'month' to categorical
    #     self.df['month'] = self.df['month'].astype('category')

    #     # Convert 'operating_systems' to categorical
    #     self.df['operating_systems'] = self.df['operating_systems'].astype('category')

    #     # Convert 'browser' to categorical
    #     self.df['browser'] = self.df['browser'].astype('category')

    #     # Convert 'region' to categorical
    #     self.df['region'] = self.df['region'].astype('category')

    #     # Convert 'traffic_type' to categorical
    #     self.df['traffic_type'] = self.df['traffic_type'].astype('category')

    #     # Convert 'visitor_type' to categorical
    #     self.df['visitor_type'] = self.df['visitor_type'].astype('category')

    #     # Convert 'weekend' to boolean
    #     self.df['weekend'] = self.df['weekend'].astype('bool')

    #     # Convert 'revenue' to boolean
    #     self.df['revenue'] = self.df['revenue'].astype('bool')

    #     # Convert numeric columns to appropriate numeric types
    #     self.df['administrative'] = pd.to_numeric(self.df['administrative'], errors='coerce')
    #     self.df['administrative_duration'] = pd.to_numeric(self.df['administrative_duration'], errors='coerce')
    #     self.df['informational'] = pd.to_numeric(self.df['informational'], errors='coerce')
    #     self.df['informational_duration'] = pd.to_numeric(self.df['informational_duration'], errors='coerce')
    #     self.df['product_related'] = pd.to_numeric(self.df['product_related'], errors='coerce')
    #     self.df['product_related_duration'] = pd.to_numeric(self.df['product_related_duration'], errors='coerce')
    #     self.df['bounce_rates'] = pd.to_numeric(self.df['bounce_rates'], errors='coerce')
    #     self.df['exit_rates'] = pd.to_numeric(self.df['exit_rates'], errors='coerce')
    #     self.df['page_values'] = pd.to_numeric(self.df['page_values'], errors='coerce')

    #     return self.df


# Example usage:
# from data_transformer import DataTransformer

# Initialize the DataTransformer with a DataFrame
# transformer = DataTransformer(data)
# Perform transformations
# transformed_data = transformer.transform_method_example()
