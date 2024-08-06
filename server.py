import uvicorn
from contextlib import asynccontextmanager
from config import db_config, server_config
from globals import globals
from fastapi import FastAPI
from data_access_layer import basic_db_functions

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Actions to perform at startup
    basic_db_functions.check_and_add_allowed_topics()
    yield
    # Actions to perform at shutdown

app = FastAPI(lifespan=lifespan)

@app.get('/')
async def root():
    return 'Hello from FastAPI server'

def add_routes():
    from routes import basic_db_functions_route, openai_route
    app.include_router(basic_db_functions_route.router, prefix='/db')
    app.include_router(openai_route.router, prefix='/question')

if __name__ == "__main__":
    try:
        server_config.setup_env_vars()
        # start db configuration
        db_config.set_mongo_client()
        # start server
        add_routes()
        port = 8002 if globals.env_status == "dev" else 8001
        uvicorn.run(app, host="127.0.0.1", port=port)
        
    except Exception as e:
        print(e)
        exit(1)
        
