from flask import Flask, request
import pomodoro_core as pomodoro
import log
import threading
import sys

PORT = 3001

cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: None

app = Flask(__name__)

@app.route('/')
def ping():
    return 'pong'

@app.route('/remaining_time_info', methods=['GET'])
def get_remaining_time():
    now = pomodoro.get_timer()
    return {'restam': now}

@app.route('/actual_cycle', methods=['GET'])
def get_cycle():
    cycle = pomodoro.get_cycle()
    return {'ciclo': cycle}

@app.route('/new/session', methods=['POST'])
def new_session():
    big=int(request.args.get('big'))
    small=int(request.args.get('small'))
    time=int(request.args.get('time'))

    log.debug('nova sessão')
    pomodoro.main(time, big, small)
    return ('', 204)

def start_server():
    app.run(port=PORT, debug=False)
    log.debug('server rodando na porta 3001')