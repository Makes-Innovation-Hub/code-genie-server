from fastapi import FastAPI
from logging_pac.logging_setup import logger
app = FastAPI()


@app.get('/')
async def root():
    logger.info("this is a server test")
    return 'Hello from FastAPI server'
