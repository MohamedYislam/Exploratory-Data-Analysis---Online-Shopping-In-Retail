import yaml

class RDSDatabaseConnector:
    """
    This class will contain methods to connect to and extract data from the RDS database.
    """
    
    # Task 2 Step 4
    def __init__(self, creds):
        """
        Initialize the RDSDatabaseConnector with database credentials.
        
        Args:
            creds (dict): A dictionary containing the database credentials.
        """
        self.creds = creds  # Store the credentials as an instance attribute

    # Task 2 Step 3
    def read_db_creds(self, file_path):  
        """
        Read database credentials from a YAML file.

        Args:
            file_path (str): The path to the YAML file containing the database credentials.

        Returns:
            dict: A dictionary containing the database credentials.
        """
        with open(file_path, 'r') as f:  # Open the YAML file in read mode
            creds = yaml.safe_load(f)  # Load the YAML file contents into a dictionary
        return creds  # Return the dictionary containing the database credentials
