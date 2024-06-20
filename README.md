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

### 1. High Bounce and Exit Rates
- **Insight**: The website exhibits high bounce and exit rates, indicating that many users leave the site after viewing only one page or after a short interaction.
- **Detail**: Analysis showed that a significant portion of users left the website after visiting only the homepage or a single product page, suggesting issues with user engagement and site navigation.
- **Recommendation**: 
    - Improve the design and content of landing pages to capture user interest immediately.
    - Streamline the navigation process to make it easier for users to find what they are looking for.
    - Implement engaging content such as videos, testimonials, and interactive elements.
    - Use clear and compelling call-to-action buttons to guide users to other parts of the website.

### 2. Product-Related Engagement
- **Insight**: Users spend considerable time on product-related pages, but conversion rates vary significantly across different products.
- **Detail**: Detailed analysis indicated that while users frequently visit product pages, certain products have lower conversion rates despite high traffic, pointing to potential issues with product presentation or pricing.
- **Recommendation**:
    - Enhance product pages with high-quality images, detailed descriptions, and customer reviews to build trust and interest.
    - Use A/B testing to experiment with different layouts, pricing strategies, and promotional offers.
    - Implement personalized product recommendations based on user browsing history and preferences to increase the likelihood of conversion.

### 3. Impact of Weekends
- **Insight**: There is a noticeable increase in user activity during weekends, with more sessions and higher engagement levels.
- **Detail**: The analysis revealed spikes in website traffic and user interactions during weekends, suggesting that users are more likely to browse and shop during their leisure time.
- **Recommendation**:
    - Leverage this trend by offering special promotions, discounts, and marketing campaigns specifically targeting weekend shoppers.
    - Ensure the website is fully optimized and can handle increased traffic during peak times.
    - Consider launching new products or features on weekends to maximize visibility and engagement.

### 4. Browser and Operating System Trends
- **Insight**: Certain browsers and operating systems are more popular among users, influencing their browsing experience and engagement levels.
- **Detail**: Data analysis showed that users predominantly accessed the website using specific browsers and operating systems, which could impact their overall experience due to compatibility issues.
- **Recommendation**:
    - Ensure that the website is fully compatible with and performs optimally on the most popular browsers and operating systems identified in the analysis.
    - Conduct regular testing and optimization for these platforms to provide a seamless user experience.
    - Address any identified issues or bugs related to specific browsers or operating systems promptly.

### 5. New vs. Returning Visitors
- **Insight**: The behavior of new and returning visitors differs significantly, with returning visitors showing higher engagement and conversion rates.
- **Detail**: Analysis highlighted that returning visitors tend to spend more time on the website and are more likely to complete purchases compared to new visitors.
- **Recommendation**:
    - Develop targeted marketing strategies to attract new visitors, such as introductory offers, discounts, and targeted advertising.
    - Engage returning visitors with loyalty programs, personalized recommendations, and exclusive offers to maintain their interest and encourage repeat purchases.
    - Use retargeting campaigns to bring back visitors who left the site without completing a purchase.

### 6. Handling Missing Data
- **Insight**: Missing data was identified and appropriately handled to ensure robust analysis and accurate insights.
- **Detail**: The dataset contained missing values that could skew the analysis if not addressed. Techniques such as imputation and removal of incomplete records were employed.
- **Recommendation**:
    - Continuously monitor data quality and implement mechanisms to handle missing data in real-time.
    - Use advanced imputation techniques to fill in missing values accurately without introducing bias.
    - Ensure that data collection processes are robust and capture all necessary information to minimize missing data in the future.

By implementing these recommendations, the online shopping platform can enhance user engagement, improve the user experience, and ultimately drive higher conversion rates and sales.


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
