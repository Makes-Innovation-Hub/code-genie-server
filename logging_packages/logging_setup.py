import logging
import uuid
import os
import glob
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request


def get_file_size(file_path):
    return os.path.getsize(file_path)

#this function return the latest log file that was created
def find_latest_log_file(directory, file_extension='*.log'): 
    search_pattern = os.path.join(directory, file_extension)
    log_files = glob.glob(search_pattern)
    if not log_files:
        print("No log files found in the directory.")
        return None
    latest_log_file = max(log_files, key=os.path.getctime)
    size = os.path.getsize(latest_log_file)
    print(f"The most recently created log file is: {latest_log_file}")
    return latest_log_file
#this file get the latest log file that created and checks if we need to create a new one 
def logfile_to_send():
    last_log =find_latest_log_file('./logging_packages/logs')
    if last_log != None:
        last_log_size = get_file_size(last_log)
        log_number = ''.join([i for i in last_log if i.isdigit()])
        number = int(log_number)
        if last_log_size >= 20000:
            number +=1
    else:
        number = 0
    next_log_file= (f"log{number}.log")
    log_file = os.path.join('logging_packages','logs', next_log_file)
    return log_file

file_name = logfile_to_send()
logging.basicConfig(level = logging.DEBUG, filename = file_name, 
                    format= "%(asctime)s - %(levelname)s - %(processName)s - %(message)s")
logger = logging.getLogger("request_logger")

def generate_request_id():
    return str(uuid.uuid4())

def log_request_received(request_id):
    logger.info(f"Received request with ID {request_id}")

def log_request_handling(request_id, message):
    logger.info(f"[Request ID: {request_id}] {message}")

def log_ERROR_handling(request_id, message):
    logger.error(f"[Request ID: {request_id}] {message}")

def log_request_completed(request_id):
    logger.info(f"Completed request with ID {request_id}")

class RequestIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_id = generate_request_id()
        request.state.request_id = request_id
        #log_request_received(request_id)
        response = await call_next(request)
        #log_request_completed(request_id)
        return response


