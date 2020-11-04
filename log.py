import logging
import os


# logging configs
logging.basicConfig(format='%(asctime)s - %(name)s - %(process)d - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S', level='DEBUG', handlers=[logging.FileHandler('log.log'), logging.StreamHandler()])


def debug(message):
    logging.debug(message)

def info(message):
    logging.info(message)

def warning(message):
    logging.warning(message)

def error(message, ex=None):
    if ex is None:
        logging.error(message)
    else:
        logging.error(message, ex)