import uvicorn
from config import db_config, server_config
from data_access_layer.limit_topics import check_and_add_allowed_topics
from globals import globals
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def root():
    return 'Hello from FastAPI server'


def add_routes():
    from routes import basic_db_functions_route, openai_route, questions_to_user, users, usernames_route
    app.include_router(basic_db_functions_route.router, prefix='/db')
    app.include_router(openai_route.router, prefix='/question')
    app.include_router(questions_to_user.router, prefix='/questions-to-user')
    app.include_router(users.router, prefix='/users')
    app.include_router(usernames_route.router, prefix='/usernames')


if __name__ == "__main__":
    try:
        server_config.setup_env_vars()
        # start db configuration
        db_config.set_mongo_client()
        check_and_add_allowed_topics()
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
