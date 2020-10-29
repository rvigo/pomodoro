from setuptools import setup

setup(
    name='pomodoro',
    version='0.0.1',
    install_requires=['click', 'requests'],
    py_modules=['pomodoro', 'interface', 'log', 'win_messages', 'server',],
    entry_points='''
        [console_scripts]
        pomodoro=interface:pomodoro
    ''',
)
