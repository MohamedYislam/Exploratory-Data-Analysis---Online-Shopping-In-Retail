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
        # Create a figure with a specific size
        plt.figure(figsize=(10, 6))
        
        # Use seaborn to create a heatmap of null values in the DataFrame
        sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
        
        # Set the title of the plot
        plt.title('Distribution of Null Values in DataFrame')
        
        # Display the plot
        plt.show()

    def plot_null_percentage(self, df: pd.DataFrame):
        """
        Plot the percentage of null values in each column.

        Args:
            df (pd.DataFrame): The DataFrame to visualize.
        """
        # Calculate the percentage of null values in each column
        null_percent = df.isnull().mean() * 100
        
        # Filter columns that have any null values
        null_percent = null_percent[null_percent > 0]

        # Create a figure with a specific size
        plt.figure(figsize=(12, 6))
        
        # Use seaborn to create a bar plot of the null percentage for each column
        sns.barplot(x=null_percent.index, y=null_percent.values)
        
        # Set the title and labels of the plot
        plt.title('Percentage of Null Values by Column')
        plt.ylabel('Percentage')
        
        # Rotate the x-axis labels for better readability
        plt.xticks(rotation=45)
        
        # Display the plot
        plt.show()

    def plot_column_distribution(self, df: pd.DataFrame, column: str):
        """
        Plot the distribution of values in a specified column.

        Args:
            df (pd.DataFrame): The DataFrame to visualize.
            column (str): The column to plot.
        """
        # Create a figure with a specific size
        plt.figure(figsize=(10, 6))
        
        # Use seaborn to create a histogram of the column's values, excluding nulls
        sns.histplot(df[column].dropna(), kde=True)
        
        # Set the title and labels of the plot
        plt.title(f'Distribution of Values in {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        
        # Display the plot
        plt.show()

    def plot_skewness(self, df: pd.DataFrame, columns: list):
        """
        Plot the skewness of specified columns in the DataFrame.

        Args:
            df (pd.DataFrame): The DataFrame to visualize.
            columns (list): The list of columns to check skewness.
        """
        for column in columns:
            # Calculate skewness of the column
            skewness = df[column].skew()
            
            # Create a figure with a specific size
            plt.figure(figsize=(10, 6))
            
            # Plot the histogram of the column values
            sns.histplot(df[column].dropna(), bins=50, kde=True)
            
            # Set the title including the skewness value
            plt.title(f'Distribution of Values in {column} (Skewness: {skewness:.2f})')
            plt.xlabel(column)
            plt.ylabel('Frequency')
            
            # Display the plot
            plt.show()
