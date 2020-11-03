from functools import wraps
import log
import requests

def http_exception_handler(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        try:
            log.debug('inside decorator')
            return func(*args, **kwargs)
        except requests.exceptions.RequestException as e:
            log.error('não foi possivel conectar ao servidor')
            print('não foi possivel conectar ao servidor')
        except Exception as e:
            log.error(f'generic error: {e.message()}')
    return wrapped
            