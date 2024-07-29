from fastapi import FastAPI, Request
from logging_pac.logging_setup import logger, RequestIDMiddleware,log_request_handling
from routes import basic_db_functions_route, openai_route

app = FastAPI()
app.add_middleware(RequestIDMiddleware)

@app.get('/')
async def root(request: Request):

    request_id = request.state.request_id
    log_request_handling(request_id, "this is a new server test")
    logger.info(f"[Request ID: {request_id}] this is a new format")
    logger.info("try this one")
    return 'Hello from FastAPI server'

app.include_router(basic_db_functions_route.router, prefix='/test')
app.include_router(openai_route.router, prefix='/question')
