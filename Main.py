Simple use pynput and timing how you control ckicking or button

start with
(Main.py)


import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

TOGGLE_KEY = KeyCode(char = "q") //เปลี่ยนปุ่มที่กด

clicking = False
mouse = Controller()

def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(0.01) //ความเร็วในการกด

def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking

click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press = toggle_event) as listener:
    listener.join()
