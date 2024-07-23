from fastapi import FastAPI
from routes import basic_db_functions_route

app = FastAPI()

@app.get('/')
async def root():
    return 'Hello from FastAPI server'

app.include_router(basic_db_functions_route.router, prefix='/test')
