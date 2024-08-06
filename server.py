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
    from routes import basic_db_functions_route, openai_route, questions_to_user, users
    app.include_router(basic_db_functions_route.router, prefix='/db')
    app.include_router(openai_route.router, prefix='/question')
    app.include_router(questions_to_user.router, prefix='/questions-to-user')
    app.include_router(users.router, prefix='/users')

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

else:
    # This is found to work with local database and local server for faster runtime
    from pymongo import MongoClient
    from dotenv import load_dotenv
    globals.env_status = 'dev'
    load_dotenv('.env.dev')
    globals.mongo_client = MongoClient('localhost', 27017)
    add_routes()