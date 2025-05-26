import logging

logging.basicConfig(filename='pipeline/pipeline.log', level=logging.DEBUG)
def log_debug(message):
    logging.debug(message)
