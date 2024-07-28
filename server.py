from fastapi import FastAPI
from routes import basic_db_functions_route, openai_route

app = FastAPI()

@app.get('/')
async def root():
    return 'Hello from FastAPI server'

app.include_router(basic_db_functions_route.router, prefix='/test')
app.include_router(openai_route.router, prefix='/question')
