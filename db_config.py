import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Store .env variables for default database
# Keeps database credentials hidden
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
DEFAULT_DB_NAME = os.getenv('DEFAULT_DBNAME')
DB_NAME = os.getenv('DBNAME')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')

# Creates default connection string
default_conn_string = f'host={HOST} dbname={
    DEFAULT_DB_NAME} user={USER} password={PASSWORD}'

conn_string = f'host={HOST} dbname={
    DB_NAME} user={USER} password={PASSWORD}'
