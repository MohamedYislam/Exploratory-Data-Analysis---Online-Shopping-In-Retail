import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Plotter:
    """
    A class for generating plots to visualize DataFrame transformations.
    """

    def plot_null_distribution(self, df: pd.DataFrame):
        """
        Plot the distribution of null values in the DataFrame.

        Args:
            df (pd.DataFrame): The DataFrame to visualize.
        """
        plt.figure(figsize=(10, 6))
        sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
        plt.title('Distribution of Null Values in DataFrame')
        plt.show()

    def plot_null_percentage(self, df: pd.DataFrame):
        """
        Plot the percentage of null values in each column.

        Args:
            df (pd.DataFrame): The DataFrame to visualize.
        """
        null_percent = df.isnull().mean() * 100
        null_percent = null_percent[null_percent > 0]

        plt.figure(figsize=(12, 6))
        sns.barplot(x=null_percent.index, y=null_percent.values)
        plt.title('Percentage of Null Values by Column')
        plt.ylabel('Percentage')
        plt.xticks(rotation=45)
        plt.show()

    def plot_column_distribution(self, df: pd.DataFrame, column: str):
        """
        Plot the distribution of values in a specified column.

        Args:
            df (pd.DataFrame): The DataFrame to visualize.
            column (str): The column to plot.
        """
        plt.figure(figsize=(10, 6))
        sns.histplot(df[column].dropna(), kde=True)
        plt.title(f'Distribution of Values in {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()
