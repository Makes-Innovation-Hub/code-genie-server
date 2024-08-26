from pymongo import MongoClient
from globals import globals
import os
from urllib.parse import quote_plus
from fastapi import Request
from logging_packages.logging_setup import logger, RequestIDMiddleware,log_request_handling



def set_mongo_client():
    logger.info("starting a new server ")
    try:
        mongodb_username = quote_plus(os.getenv('MONGODB_USERNAME'))
        mongodb_password = quote_plus(os.getenv('MONGODB_PASSWORD'))
        mongodb_host = os.getenv('MONGODB_HOST')
        if mongodb_username and mongodb_password and mongodb_host:
            mongodb_url = f'mongodb+srv://{mongodb_username}:{mongodb_password}@{mongodb_host}'
            client = MongoClient(mongodb_url)
            globals.mongo_client = client
            logger.info("connected to mongo DB ")
            return
        else:
            logger.info("one or more of mongo DB env var keys is not found")
            raise KeyError("one or more of mongo env var keys is not found")
    except Exception as e:
        logger.info(f"error in mongo initial setup: {e}")
        raise e
    