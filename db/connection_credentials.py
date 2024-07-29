import argparse
from urllib.parse import quote_plus
from dotenv import load_dotenv
from globals import globals
import os

# Load the appropriate .env file
if globals.env_status == "dev":
    load_dotenv('.env.dev')
else:
    load_dotenv('.env.prod')

mongodb_username = quote_plus(os.getenv('MONGODB_USERNAME'))
mongodb_password = quote_plus(os.getenv('MONGODB_PASSWORD'))
mongodb_host = os.getenv('MONGODB_HOST')
mongodb_url = f'mongodb+srv://{mongodb_username}:{mongodb_password}@{mongodb_host}'
