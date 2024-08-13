from fastapi import FastAPI, Request
from logging_packages.logging_setup import logger, RequestIDMiddleware,log_request_handling
from routes import basic_db_functions_route, openai_route
from config import db_config, server_config
from globals import globals
import uvicorn
app = FastAPI()
app.add_middleware(RequestIDMiddleware)


@app.get('/')
async def root(request: Request):

    request_id = request.state.request_id
    log_request_handling(request_id, "get message from the server ")
    logger.info(f"[Request ID: {request_id}] this is a new format")
    return 'Hello from FastAPI server'

def add_routes():
    from routes import basic_db_functions_route, openai_route, questions_to_user, users
    app.include_router(basic_db_functions_route.router, prefix='/db')
    app.include_router(openai_route.router, prefix='/question')
    app.include_router(questions_to_user.router, prefix='/questions-to-user')
    app.include_router(users.router, prefix='/users')

if __name__ == "__main__":
    try:
       
        logger.info("Starting a new server")
        # start db configuration
        db_config.set_mongo_client()
        # start server
        add_routes()
        port = 8002 if globals.env_status == "dev" else 8001
        uvicorn.run(app, host="127.0.0.1", port=port)        
    except Exception as e:
        logger.info(e)
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