import ctypes
import time
import argparse
import log
import sys
import os
from datetime import datetime

# consts
ALWAYS_ON_TOP = 4096
ICON_STOP = 0x10
YES_NO = 0x04
ctime = 25
small_break = 10
big_break = 30
counter = 1
session_counter = 0
verbose = False


def message_box(text, box_type=ALWAYS_ON_TOP):
    now = datetime.now()
    formatted_now = now.strftime("%d/%m/%Y %H:%M:%S")
    full_text = f'{formatted_now}\n\n\n{text}'
    return ctypes.windll.user32.MessageBoxW(0, full_text, "Pomodoro", box_type)


def countdown(time_in_seconds):
    while time_in_seconds:
        m, s = divmod(time_in_seconds, 60)
        h, m = divmod(m, 60)
        timer = f'{h:02d}:{m:02d}:{s:02d}'

        verbose and print(timer, end='\r')

        time.sleep(1)
        time_in_seconds -= 1


def core():
    global session_counter
    while 1:
        log.debug(f'ciclo {counter}')
        countdown(ctime)
        break_core()
        session_counter += 1
        validate_new_cycle()


def validate_new_cycle():
    value = value = message_box(
        f'Fim da pausa! \nDeseja realizar um novo ciclo?', YES_NO)
    if value is 7:
        sys.exit()


def break_core():
    global counter
    if counter is 4:
        log.info('big break')
        message_box(f'faça uma pausa de {big_break/60} minutos')
        counter = 0
        countdown(big_break)

    else:
        log.info('small break')
        message_box(f'faça uma pausa de {small_break/60} minutos')
        counter += 1
        countdown(small_break)


def main(parser):
    log.debug('iniciando nova sessão de trabalho')
    # globals
    global ctime
    global big_break
    global small_break
    global verbose

    args = parser.parse_args()

    # parsing to minutes
    ctime = (args.time * 60)
    big_break = (args.big * 60)
    small_break = (args.small * 60)
    verbose = args.verbose

    log.debug(f'ctime is {ctime}')
    log.debug(f'big break is {big_break}')
    log.debug(f'small break is {small_break}')

    # start
    core()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-b', '--big', help='valor do intervalo maior (em minutos)', type=int, default=30)
    parser.add_argument(
        '-s', '--small', help='valor do intervalo menor (em minutos)', type=int, default=5)
    parser.add_argument(
        '-t', '--time', help='valor do ciclo (em minutos)', type=int, default=25)
    parser.add_argument(
        '-v', '--verbose', help='modo verboso', action='store_true')

    try:
        print(f'starting at PID {os.getpid()}')
        main(parser)
    except KeyboardInterrupt:
        print(end='\r')
        sys.exit()
    except Exception as e:
        log.error(e)
    finally:
        log.debug('fim da sessão')
        log.debug(f'total de ciclos na sessão: {session_counter}')
