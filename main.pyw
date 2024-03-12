from win32con import MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP
from keyboard import is_pressed, block_key
from win32api import mouse_event
from random import uniform
from time import sleep


def click():
    mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(uniform(0.01, 0.07))
    mouse_event(MOUSEEVENTF_LEFTUP, 0, 0)
    sleep(uniform(0.01, 0.07))


block_key("f24")
block_key("f20")

while True:
    if is_pressed("f24"):
        click()
    if is_pressed("f20"):
        break
    sleep(0.000001)
