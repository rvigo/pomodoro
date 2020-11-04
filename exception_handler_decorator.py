from functools import wraps
import log
import requests

def http_exception_handler(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except requests.exceptions.RequestException as e:
            log.error('não foi possivel conectar ao servidor')
    return wrapped
            