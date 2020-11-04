from setuptools import setup

setup(
    name='pomodoro',
    version='0.0.1',
    install_requires=['click', 'requests'],
    py_modules=['pomodoro', 'pomodoro_core', 'log', 'win_messages', 'server', 'exception_handler_decorator'],
    entry_points='''
        [console_scripts]
        pomodoro=pomodoro:pomodoro
    ''',
)
