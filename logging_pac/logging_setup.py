import logging
logging.basicConfig(level = logging.DEBUG, filename = "log0.log", 
                    format= "%(asctime)s - %(levelname)s - %(message)s")

logger = logging.getLogger(__name__)
logger.info("this is a test")