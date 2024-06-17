from db_utils import RDSDatabaseConnector
from data_extraction import DataExtractor
from data_transformer import DataTransformer
from data_frame_info import DataFrameInfo
import pandas as pd
"""
# Path to the credentials file
yaml_file = "credentials.yaml"

# Initialize the database connector
db_connector = RDSDatabaseConnector(yaml_file)

# Initialize the data extractor with the database connector's engine
data_extractor = DataExtractor(db_connector.engine)

# Task 3 Step 6: Extract data from the 'customer_activity' table
table_name = "customer_activity"
data = data_extractor.read_rds_table(table_name)


print(data, "<data")
print(data.info(), "<data.info()")
for column in data.columns:
    print(data[column], f"\n<data['{column}']")
    print(data[column].unique(), f"\n<data['{column}'.unique()]")


#Task 3 Step 7: Save the data to a CSV file
csv_file_path = "customer_activity.csv"
data_extractor.save_to_csv(data, csv_file_path)

print(f"Data saved to {csv_file_path}")
"""
csv_file_path = "customer_activity.csv"
data = pd.read_csv(csv_file_path)

# print(data, "<data")

for column in data.columns:
    print(data[column], f"\n<data['{column}']")
    print(data[column].unique(), f"\n<data['{column}'.unique()]")
# print(data.info(), "<data.info() before cleaning")
data_transformer = DataTransformer(data)
# print(data_transformer, "<data_transformer")
cleaned_data = data_transformer.clean_and_convert_columns()
# print(data.info(), "<data.info() before cleaning")
# print(cleaned_data.info(), "<cleaned_data.info() after cleaning")

df_info = DataFrameInfo(cleaned_data)
# val = df_info.describe_columns()
# print(val, "<val")
# print(val.month, "<val.month")
df_info.statistics("aojgea")
