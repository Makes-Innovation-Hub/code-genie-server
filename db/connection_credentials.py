from urllib.parse import quote_plus
from dotenv import load_dotenv
import os

load_dotenv()

mongodb_username = quote_plus(os.getenv('MONGODB_USERNAME'))
mongodb_password = quote_plus(os.getenv('MONGODB_PASSWORD'))
mongodb_url = f'mongodb+srv://{mongodb_username}:{mongodb_password}@telegrambot.ztcvwep.mongodb.net/?retryWrites=true&w=majority&appName=telegrambot'
