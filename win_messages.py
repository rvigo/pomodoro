import  ctypes
from datetime import datetime

#consts
ALWAYS_ON_TOP = 4096

def message_box(text, box_type=ALWAYS_ON_TOP):
    now = datetime.now()
    formatted_now = now.strftime("%d/%m/%Y %H:%M:%S")
    full_text = f'{formatted_now}\n\n\n{text}'
    return ctypes.windll.user32.MessageBoxW(0, full_text, "Pomodoro", box_type)
