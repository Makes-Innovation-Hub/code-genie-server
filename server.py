from fastapi import FastAPI
<<<<<<< HEAD
from logging_pac.logging_setup import logger
=======
from routes import basic_db_functions_route, openai_route

>>>>>>> 7e6bc1b47a5308cbd9306e671ecdcf402c3bea4e
app = FastAPI()

@app.get('/')
async def root():
    logger.info("this is a server test")
    return 'Hello from FastAPI server'

app.include_router(basic_db_functions_route.router, prefix='/test')
app.include_router(openai_route.router, prefix='/question')
