from db_utils import RDSDatabaseConnector
from data_extraction import DataExtractor

# Path to the credentials file
yaml_file = "credentials.yaml"

# Initialize the database connector
db_connector = RDSDatabaseConnector(yaml_file)

# Initialize the data extractor with the database connector's engine
data_extractor = DataExtractor(db_connector.engine)

# Task 3 Step 6: Extract data from the 'customer_activity' table
table_name = "customer_activity"
data = data_extractor.read_rds_table(table_name)

# print(data.info(), "<data.info()")
# print(data['administrative'], "<data['adminstrative']")
# print(data['administrative_duration'], "<adminstrative_duration")
# print(data['informational'], "<data['informational']")

# print(data['visitor_type'], "<data[visitor_type]")
# print(data['revenue'], "<data[revenue]")
print(data, "<data")
print(data.info(), "<data.info()")
for column in data.columns:
    print(data[column], f"\n<data['{column}']")
    print(data[column].unique(), f"\n<data['{column}'.unique()]")


#Task 3 Step 7: Save the data to a CSV file
csv_file_path = "customer_activity.csv"
data_extractor.save_to_csv(data, csv_file_path)

print(f"Data saved to {csv_file_path}")

#