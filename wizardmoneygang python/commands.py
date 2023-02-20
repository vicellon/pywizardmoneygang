import pyautogui as pyg
import time as t
import keyboard
import numpy as n
import random as rand
import win32api, win32con
import smtplib
import os

import values

def setspawn():
    print("setting spawn...")
    pyg.press('t')
    pyg.write("/setspawn")
    pyg.press('enter')
    print("spawn set!")

def island_return():
    print("returning...")
    pyg.press('t')
    pyg.write("/is")
    pyg.press('enter')
    t.sleep(5)
    print("returned!")
    pyg.keyDown('shift')
    t.sleep(1)
    pyg.keyUp('shift')
    values.times_returned += 1