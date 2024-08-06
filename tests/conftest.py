import pytest
import os
from dotenv import load_dotenv
from globals import globals
from config import db_config 


@pytest.fixture(scope="session", autouse=True)
def setup():
    load_env_vars()
    db_config.set_mongo_client()

def load_env_vars():
    env = globals.env_status or "dev" # need to fix to allow prod testing too
    try:
        file_path = f".env.{env}"
        if os.path.isfile(file_path):
            load_dotenv(file_path)
        else:
            raise ValueError("could not load envs")
    except Exception as e:
        print(e)
        raise e
