import time
import argparse
import log
import sys
import os
import win_messages

# consts
ICON_STOP = 0x10
YES_NO = 0x04
ctime = 0
small_break = 0
big_break = 0
counter = 1
session_counter = 1
timer = ''


def get_timer() -> str:
    if timer is '':
        return 'o contador ainda não foi iniciado!S'
    return timer


def get_cycle() -> str:
    return session_counter


def countdown(time_in_seconds):
    global timer
    while time_in_seconds:
        m, s = divmod(time_in_seconds, 60)
        h, m = divmod(m, 60)
        timer = f'{h:02d}:{m:02d}:{s:02d}'
        time.sleep(1)
        time_in_seconds -= 1


def core():
    global session_counter
    loop_flag = True
    while loop_flag:
        log.debug(f'Ciclo {counter}')
        countdown(ctime)
        break_core()
        session_counter += 1
        if(not validate_new_cycle()):
            reset_consts()
            loop_flag = False


def reset_consts():
    global session_counter
    global counter
    global ctime
    global big_break
    global small_break
    global timer

    session_counter = 1
    counter = 1
    ctime = 0
    big_break = 0
    small_break = 0
    timer = ''


def validate_new_cycle():
    value = value = win_messages.message_box(
        f'Fim da pausa! \nDeseja realizar um novo ciclo?', YES_NO)
    # 7 is the NO result
    if value is 7:
        return False


def break_core():
    global counter
    if counter is 4:
        log.info('big break')
        win_messages.message_box(f'Faça uma pausa de {big_break/60} minutos')
        counter = 0
        countdown(big_break)

    else:
        log.info('small break')
        win_messages.message_box(f'Faça uma pausa de {small_break/60} minutos')
        counter += 1
        countdown(small_break)


def main(t, big, small):
    print(f'PID {os.getpid()}')

    log.debug('iniciando nova sessão de trabalho')
    # globals
    global ctime
    global big_break
    global small_break

    # parsing to minutes
    ctime = (t * 60)
    big_break = (big * 60)
    small_break = (small * 60)

    # start
    core()