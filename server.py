import argparse
import uvicorn
import os
from config import db_config, server_config
from globals import globals
from fastapi import FastAPI
from routes import basic_db_functions_route, openai_route

app = FastAPI()

@app.get('/')
async def root():
    return 'Hello from FastAPI server'

app.include_router(basic_db_functions_route.router, prefix='/db')
app.include_router(openai_route.router, prefix='/question')

if __name__ == "__main__":
    try:
        server_config.setup_env_vars()
        # start db configuration
        db_config.set_mongo_client()
        # start server
        port = 8002 if globals.env_status == "dev" else 8001
        uvicorn.run("server:app", host="127.0.0.1", port=port, reload=True, reload_dirs=["."])
        
    except Exception as e:
        print(e)
        exit(1)
        
