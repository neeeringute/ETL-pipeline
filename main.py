import warnings
warnings.filterwarnings('ignore')

from datetime import datetime
from src.extract import extract_transactional_data
from src.transform import identify_and_remove_duplicates
from src.load_data_to_s3 import df_to_s3

start_time = datetime.now()

# this library is being used to read from the .env file
import os
from dotenv import load_dotenv
load_dotenv()

# reading the variables from the .env file
dbname = os.getenv("dbname")
port = os.getenv("port")
host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
# reading the variables that will connect to s3
key='transformations_final/ne_online_trans_transformed.pkl'
s3_bucket="sep-bootcamp"
aws_access_key_id=os.getenv("aws_access_key_id")
aws_secret_access_key=os.getenv("aws_secret_access_key_id")


# step 1: extract and transform the data
print("\nExtracting the data from redshift...")
ot_transformed = extract_transactional_data(dbname, host, port, user, password)

# step 2: identify and remove duplicate
print("\nIdentifying and removing duplicates")
ot_wout_duplicates = identify_and_remove_duplicates(ot_transformed)

# step 3: load data to s3
print("\nLoading data to s3 bucket")
df_to_s3(ot_wout_duplicates, key, s3_bucket, aws_access_key_id, aws_secret_access_key)

# if you want to you can calculate
execution_time = datetime.now() - start_time
print(f"Total execution time (hh:mm:ss) {execution_time}")