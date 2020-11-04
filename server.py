from flask import Flask, request
import pomodoro_core as pomodoro
import log
import threading
import sys

PORT = 3001

cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: None

app = Flask(__name__)

@app.route('/ping')
def ping():
    return 'pong'

@app.route('/session/timer', methods=['GET'])
def get_remaining_time():
    now = pomodoro.get_timer()
    return {'restam': now}

@app.route('/session/cycle', methods=['GET'])
def get_cycle():
    cycle = pomodoro.get_cycle()
    return {'ciclo': cycle}

@app.route('/session', methods=['POST'])
def new_session():
    big=int(request.args.get('big'))
    small=int(request.args.get('small'))
    time=int(request.args.get('time'))

    log.debug(f'Nova sessão: tempo: {time}, intervalo maior: {big}, intervalo menor:{small}')
    pomodoro.main(time, big, small)
    return ('', 204)

def start_server():
    app.run(port=PORT, debug=False)
    log.info(f'Server rodando na porta {PORT}')