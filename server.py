import argparse
import uvicorn
import os

from globals import globals
from dotenv import load_dotenv
from fastapi import FastAPI
from routes import basic_db_functions_route, openai_route

app = FastAPI()

@app.get('/')
async def root():
    return 'Hello from FastAPI server'

app.include_router(basic_db_functions_route.router, prefix='/test')
app.include_router(openai_route.router, prefix='/question')

if __name__ == "__main__":
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
        if globals.env_status == "dev":
            uvicorn.run(app, host="127.0.0.1", port=8002)
        else:
            uvicorn.run(app, host="127.0.0.1", port=8001)
        
    except Exception as e:
        print(e)
        exit(1)
        
