import pytest
import os
from dotenv import load_dotenv
from globals import globals
from config import db_config 

def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="dev",
        help="Specify the environment: dev or prod"
    )

@pytest.fixture(scope="session", autouse=True)
def setup(pytestconfig):
    load_env_vars(pytestconfig)
    db_config.set_mongo_client()

def load_env_vars(pytestconfig):
    env = pytestconfig.getoption('env')
    try:
        file_path = f".env.{env}"
        if os.path.isfile(file_path):
            load_dotenv(file_path)
        else:
            raise ValueError("could not load envs")
    except Exception as e:
        print(e)
        raise e
