import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import boxcox, probplot
import math
from typing import List

class Plotter:
    """
    A class for generating plots to visualize DataFrame transformations.
    """

    def plot_null_distribution(self, df: pd.DataFrame) -> None:
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

    def plot_null_percentage(self, df: pd.DataFrame) -> None:
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

    def plot_column_distribution(self, df: pd.DataFrame, column: str) -> None:
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

    def plot_skewness(self, df: pd.DataFrame, columns: List[str]) -> None:
        """
        Plot the skewness of specified columns in the DataFrame.

        Args:
            df (pd.DataFrame): The DataFrame to visualize.
            columns (List[str]): The list of columns to check skewness.
        """
        # Number of columns for the grid
        num_columns = len(columns)
        num_rows = math.ceil(num_columns / 3)

        # Create subplots with a specific size
        fig, axes = plt.subplots(num_rows, 3, figsize=(20, num_rows * 6))

        # Flatten axes array for easy iteration
        axes = axes.flatten()

        for idx, column in enumerate(columns):
            # Select the axis for the current plot
            ax = axes[idx]

            # Calculate skewness of the column
            skewness = df[column].skew()

            # Plot the histogram of the column values
            sns.histplot(df[column].dropna(), bins=50, kde=True, ax=ax)

            # Set the title including the skewness value
            ax.set_title(f'Distribution of Values in {column} (Skewness: {skewness:.2f})')
            ax.set_xlabel(column)
            ax.set_ylabel('Frequency')

        # Hide any unused subplots
        for i in range(num_columns, len(axes)):
            fig.delaxes(axes[i])

        # Adjust layout
        fig.tight_layout()

        # Display the plot
        plt.show()

    def plot_qq(self, df: pd.DataFrame, columns: List[str]) -> None:
        """
        Plot Q-Q plots of the specified columns in a grid format.

        Args:
            df (pd.DataFrame): The DataFrame to visualize.
            columns (List[str]): The list of columns to plot.
        """
        # Number of columns for the grid
        num_columns = len(columns)
        num_rows = math.ceil(num_columns / 3)

        # Create subplots with a specific size
        fig, axes = plt.subplots(num_rows, 3, figsize=(20, num_rows * 6))

        # Flatten axes array for easy iteration
        axes = axes.flatten()

        for idx, column in enumerate(columns):
            # Select the axis for the current plot
            ax = axes[idx]

            # Create Q-Q plot
            probplot(df[column].dropna(), dist="norm", plot=ax)
            
            # Set the color of the Q-Q plot line to red
            ax.get_lines()[1].set_color('red')
            
            # Set the title of the subplot
            ax.set_title(f'Q-Q Plot of {column}')

        # Hide any unused subplots
        for i in range(num_columns, len(axes)):
            fig.delaxes(axes[i])

        # Adjust layout
        fig.tight_layout()

        # Display the plot
        plt.show()

    def plot_categorical_data(self, df: pd.DataFrame, categorical_columns: List[str]) -> None:
        """
        Plot bar charts for categorical columns in a grid format.

        Args:
            df (pd.DataFrame): The DataFrame to visualize.
            categorical_columns (List[str]): List of categorical columns to plot.
        """
        # Number of plots per row
        num_columns = 3
        num_rows = math.ceil(len(categorical_columns) / num_columns)
        
        # Create subplots with a specific size
        fig, axes = plt.subplots(num_rows, num_columns, figsize=(num_columns * 5, num_rows * 5))
        
        # Flatten axes array for easy iteration
        axes = axes.flatten()
        
        for i, column in enumerate(categorical_columns):
            # Use seaborn to create a count plot for each categorical column
            sns.countplot(data=df, x=column, ax=axes[i])
            
            # Set the title and labels of the plot
            axes[i].set_title(f'Distribution of {column}')
            axes[i].set_ylabel('Count')
            axes[i].set_xlabel(column)
        
        # Remove any empty subplots
        for j in range(i + 1, len(axes)):
            fig.delaxes(axes[j])
        
        # Adjust layout
        plt.tight_layout()
        
        # Display the plot
        plt.show()

    def plot_boxplots(self, df: pd.DataFrame, columns: List[str], rows: int = 2, cols: int = 3, figsize: tuple = (15, 10)) -> None:
        """
        Plot boxplots for the specified columns.

        Args:
            df (pd.DataFrame): The DataFrame to visualize.
            columns (List[str]): List of columns to plot.
            rows (int): Number of rows in the grid.
            cols (int): Number of columns in the grid.
            figsize (tuple): Size of the figure.
        """
        # Create subplots with a specific size
        fig, axes = plt.subplots(rows, cols, figsize=figsize)
        
        # Flatten axes array for easy iteration
        axes = axes.flatten()

        for i, col in enumerate(columns):
            # Use seaborn to create a boxplot for each column
            sns.boxplot(y=df[col], ax=axes[i])
            
            # Set the title of the plot
            axes[i].set_title(col)

        # Hide any unused subplots
        for i in range(len(columns), len(axes)):
            fig.delaxes(axes[i])

        # Adjust layout
        plt.tight_layout()
        
        # Display the plot
        plt.show()

    def correlation_matrix(self, df: pd.DataFrame) -> None:
        """
        Plot a heatmap of the correlation matrix of the DataFrame.

        Args:
            df (pd.DataFrame): The DataFrame to visualize.
        """
        # Calculate the correlation matrix
        corr = df.corr()
        
        # Create a figure with a specific size
        plt.figure(figsize=(12, 10))
        
        # Use seaborn to create a heatmap of the correlation matrix
        sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', linewidths=0.5)
        
        # Set the title of the plot
        plt.title('Correlation Matrix')
        
        # Display the plot
        plt.show()

    def plot_bar_chart(self, df: pd.DataFrame, title: str, xlabel: str, ylabel: str) -> None:
        """
        Plot a bar chart.

        Args:
            df (pd.DataFrame): The DataFrame containing the data.
            title (str): Title of the chart.
            xlabel (str): Label for the x-axis.
            ylabel (str): Label for the y-axis.
        """
        # Create a figure with a specific size
        plt.figure(figsize=(12, 6))
        
        # Use seaborn to create a bar plot
        sns.barplot(x=df.index, y=df.values, palette="viridis")

        # Set the title and labels of the plot
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        
        # Rotate the x-axis labels for better readability
        plt.xticks(rotation=45)

        # Display the plot
        plt.show()

    def plot_stacked_bar_chart(self, df: pd.DataFrame, title: str, xlabel: str, ylabel: str) -> None:
        """
        Plot a stacked bar chart.

        Args:
            df (pd.DataFrame): The DataFrame containing the data with a multi-index (region, traffic_type).
            title (str): Title of the chart.
            xlabel (str): Label for the x-axis.
            ylabel (str): Label for the y-axis.
        """
        # Reset the index to plot the multi-index DataFrame
        df = df.unstack(level=-1)
        
        # Plot the DataFrame as a stacked bar chart
        df.plot(kind='bar', stacked=True, figsize=(12, 6), colormap='viridis')

        # Set the title and labels of the plot
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        
        # Rotate the x-axis labels for better readability
        plt.xticks(rotation=45)
        
        # Display the plot
        plt.show()
