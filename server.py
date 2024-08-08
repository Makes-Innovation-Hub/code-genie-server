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
    from routes import basic_db_functions_route, openai_route
    app.include_router(basic_db_functions_route.router, prefix='/db')
    app.include_router(openai_route.router, prefix='/question')

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
        print(e)
        exit(1)
        
