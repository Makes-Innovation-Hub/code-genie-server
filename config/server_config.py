from globals import globals
import argparse
import os
from dotenv import load_dotenv

def setup_env_vars():
    parser = argparse.ArgumentParser(description="FastAPI server")
    parser.add_argument('--env', type=str, default='dev', help='Environment (choices: dev, prod, default: dev)')
    args = parser.parse_args()

    if args.env not in ["dev", "prod"]:
        raise ValueError("Invalid environment! Choose either 'dev' or 'prod'.")
    
    globals.env_status = args.env
    
     # Load the appropriate .env file
    try:
        file_path = f".env.{globals.env_status}"
        if os.path.isfile(file_path):
            load_dotenv(file_path)
            print(f"Starting server in {globals.env_status} environment")
        else:
            raise FileExistsError(f"Could not find .env file: {file_path}")
    except FileExistsError as e:
        raise e
    except Exception as e:
        print(f"error in loading env vars",e)
        raise e