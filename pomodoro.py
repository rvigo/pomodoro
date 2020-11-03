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
    click.echo(requests.get(f'http://{URL}/remaining_time_info').text) 
    
@pomodoro.command()
@http_exception_handler
def cycle():
    click.echo(requests.get(f'http://{URL}/actual_cycle').text) 
    
@pomodoro.command()
@click.option('--time','-t', type=int, required=True)
@click.option('--small','-s', type=int, required=True)
@click.option('--big','-b', type=int, required=True)
@http_exception_handler
def start(time, big, small):
    log.debug('validando status do servidor')
    global IS_SERVER_ON
    if not IS_SERVER_ON:
        log.debug('servidor desligado. Iniciando servidor na porta 3001')  
        bootup()
        IS_SERVER_ON=True
    
    route= f'http://{URL}/new/session?big={big}&small={small}&time={time}'
    r = requests.post(route)
    click.echo(r.text)  
    
@pomodoro.command()
@http_exception_handler
def run():
    global IS_SERVER_ON
    if not IS_SERVER_ON:
        log.debug('servidor desligado. Iniciando servidor na porta 3001')  
        bootup()
        IS_SERVER_ON=True
        
        ##TODO validar outra abordagem para o start do servidor http
           
def bootup():
    threading.Thread(target=server.start_server).start()

if __name__ == "__main__":
    pomodoro()