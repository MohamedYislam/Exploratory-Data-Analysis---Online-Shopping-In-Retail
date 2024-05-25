import yaml
from sqlalchemy import create_engine, inspect, URL
from sqlalchemy.exc import SQLAlchemyError, PendingRollbackError


class RDSDatabaseConnector:
    """
    This class will contain methods to connect to and extract data from the RDS database.
    """
    
    # Task 2 Step 4
    def __init__(self, creds_file_path):
        """
        Initialize the RDSDatabaseConnector with database credentials.
        
        Args:
            creds_file_path (str): The file path to the database credentials.
        """
        self.creds = self._read_db_creds(creds_file_path)
        self.engine = self._init_db_engine()

    # Task 2 Step 3
    def _read_db_creds(self, file_path):
        """
        Read database credentials from a YAML file.

        Args:
            file_path (str): The path to the YAML file containing the database credentials.

        Returns:
            dict: A dictionary containing the database credentials.
        """
        with open(file_path, 'r') as f:
            creds = yaml.safe_load(f)
        return creds

    # Task 2 Step 5
    def _init_db_engine(self):
        """
        Initialize the database engine using the database credentials.

        Returns:
            sqlalchemy.engine.Engine: The initialized database engine.
        """
        url_object = URL.create(
            "postgresql",
            username=self.creds['RDS_USER'],
            password=self.creds['RDS_PASSWORD'],
            host=self.creds['RDS_HOST'],
            database=self.creds['RDS_DATABASE'],
        )
        engine = create_engine(url_object)
        return engine


yaml_file = "credentials.yaml"
test_connector = RDSDatabaseConnector(yaml_file)

print(test_connector)
print(test_connector.creds)
print(test_connector.engine, "<test_connector.engine")
