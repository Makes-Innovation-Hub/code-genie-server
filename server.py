import argparse
import uvicorn
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
    globals.env_status = args.env

    if globals.env_status not in ["dev", "prod"]:
        raise ValueError("Invalid environment! Choose either 'dev' or 'prod'.")
        
    print(f"Starting server in {globals.env_status} environment")

    # Load the appropriate .env file
    # run the appropriate server
    if globals.env_status == "dev":
        load_dotenv('.env.dev')
        uvicorn.run(app, host="127.0.0.1", port=8002)
    else:
        load_dotenv('.env.prod')
        uvicorn.run(app, host="127.0.0.1", port=8001)
    