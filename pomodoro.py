import click
import pomodoro_core as p
import log
import server
import requests
from time import sleep
import threading
from exception_handler_decorator import http_exception_handler

IS_SERVER_ON=False
HOSTNAME = 'localhost'
PORT=3001

URL = f'{HOSTNAME}:{PORT}'

@click.group()
def pomodoro():
    pass

@pomodoro.command()
@http_exception_handler
def timer():
    click.echo(requests.get(f'http://{URL}/session/timer').text) 
    
@pomodoro.command()
@http_exception_handler
def cycle():
    click.echo(requests.get(f'http://{URL}/session/cycle').text) 
    
@pomodoro.command()
@click.option('--time','-t', type=int, required=True)
@click.option('--small','-s', type=int, required=True)
@click.option('--big','-b', type=int, required=True)
@http_exception_handler
def start(time, big, small):
    log.debug('Validando status do servidor')
    run()
    route= f'http://{URL}/session?big={big}&small={small}&time={time}'
    r = requests.post(route)
    click.echo(r.text)  
    
@pomodoro.command()
@http_exception_handler
def run():
    global IS_SERVER_ON
    if not IS_SERVER_ON:
        log.debug('Servidor desligado. Iniciando servidor na porta 3001')  
        bootup()
        ping = requests.get(f'http://{URL}/ping').text
        if ping is 'pong':
            IS_SERVER_ON=True
        else:
            log.error('Ocorreu um erro ao ligar o servidor')   
            
def bootup():
    threading.Thread(target=server.start_server).start()

if __name__ == "__main__":
    pomodoro()