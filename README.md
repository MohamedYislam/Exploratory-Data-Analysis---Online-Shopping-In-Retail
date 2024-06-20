# Online Shopping Website Activity Analysis

## Table of Contents
- [Description](#description)
- [Tech stack] (#tech_stack)
- [Installation](#installation)
- [Usage](#usage)
- [Business Insights](#Business_Insights)
- [File Structure](#file_structure)
- [License](#license)

## Description

This project involves conducting an exploratory data analysis (EDA) on a dataset of online shopping website activity. The aim is to derive meaningful insights into consumer behavior and help a large retail company optimize its marketing strategies and improve customer experience.

By leveraging various statistical and visualization techniques, this analysis will provide a deeper understanding of customer interactions with the website, identify patterns and trends, and suggest potential improvements. The data spans one year and includes multiple features related to user interactions during shopping sessions.

Key objectives of this project:
- To uncover valuable insights from the dataset through EDA.
- To understand user behavior and website activity.
- To suggest improvements for enhancing marketing strategies and customer experience.

In the process of completing this project, I enhanced my skills in data extraction, transformation, and visualization, as well as improved my proficiency in Python programming and various data analysis libraries.


## Tech Stack

- **Python**: Core programming language used for data manipulation and analysis.
- **Pandas**: Data manipulation and analysis.
- **NumPy**: Numerical computing.
- **Matplotlib & Seaborn**: Data visualization.
- **SQLAlchemy**: Database interaction.
- **Jupyter Notebook**: Interactive computing environment.
- **Scikit-learn**: Machine learning library for data preprocessing.
- **SciPy**: Scientific computing and technical computing.



## Installation

To install the necessary packages and set up the environment, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/MohamedYislam/Exploratory-Data-Analysis---Online-Shopping-In-Retail.git
    cd Exploratory-Data-Analysis---Online-Shopping-In-Retail
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate 
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To perform the analysis, you can run the Jupyter Notebook provided in the repository. Ensure you have Jupyter installed and start it with the following command:

```sh
jupyter notebook EDA.ipynb
```
## Business Insights

### Sales Proportion on Weekends vs. Weekdays
- **Analysis:** The analysis revealed that a significant proportion of sales occur on weekdays (79.14%), while weekends account for a smaller share (20.86%).
- **Recommendation:** Consider increasing marketing efforts and promotional campaigns on weekends to boost sales during these periods. Additionally, investigate potential factors driving higher weekday sales and see if they can be replicated or enhanced on weekends.

### Revenue by Region
- **Analysis:** The regions generating the most sales are North America (640), followed by Western Europe (279) and Eastern Europe (158). Other regions like Asia, South America, and Africa also contribute to the revenue but to a lesser extent.
- **Recommendation:** Focus marketing and expansion efforts on North America and Europe, as these regions show the highest sales potential. Tailor marketing strategies to address regional preferences and cultural differences to maximize revenue.

### Effective Website Traffic Sources for Sales
- **Analysis:** The most effective traffic sources for generating sales are Google Search (732), followed by Facebook Ads (225) and Instagram Ads (151). Other sources like Bing Search, Youtube Channel, and Affiliate Marketing contribute less significantly.
- **Recommendation:** Invest more in Google Search and social media advertising on platforms like Facebook and Instagram, as they yield the highest returns. Consider optimizing SEO strategies and expanding social media campaigns to further enhance traffic from these sources.

### Time Spent on Website Tasks
- **Analysis:** Users spend the majority of their time on product-related tasks (87.80%), with significantly less time spent on administrative (10.81%) and informational tasks (1.40%).
- **Recommendation:** Ensure that the product-related pages are optimized for user experience, with clear information, high-quality images, and easy navigation. Streamline administrative and informational tasks to minimize user frustration and enhance overall website usability.

### Breakdown of Sales by Month
- **Analysis:** Sales peak in November (740), followed by May (342) and December (274). Other months see relatively lower sales volumes.
- **Recommendation:** Prepare for high sales volumes in November and December by ensuring adequate inventory and staffing. Consider running special promotions or marketing campaigns during these peak months. Additionally, investigate the factors contributing to higher sales in May and explore opportunities to replicate this success in other months.

By understanding and acting on these key insights, the retail company can optimize its marketing strategies, improve customer experience, and ultimately drive higher sales and revenue.


## File Structure
```sh
online-shopping-activity-analysis/
│
├── data_transformer.py
├── data_extraction.py
├── data_frame_info.py
├── plotter.py
├── EDA.ipynb
├── customer_activity.csv
├── requirements.txt
├── .gitignore
└── README.md
```

• **data_transformer.py:** Used to transform and clean the data.

• **data_extraction.py:** Contains functions for extracting data from a database.

• **data_frame_info.py:** Provides various utilities for analyzing DataFrame structures and statistics.

• **plotter.py:** Used for creating visualizations of the data.

• **EDA.ipynb:** Jupyter Notebook containing the exploratory data analysis.

• **customer_activity.csv:** The dataset containing customer activity on the shopping website.

• **requirements.txt:** List of required packages for the project.

• **.gitignore:** Specifies files and directories to be ignored by Git.
README.md: Project documentation.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute this project as you wish.
