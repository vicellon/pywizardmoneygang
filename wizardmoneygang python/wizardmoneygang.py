from PIL.ImageOps import grayscale
from email.message import EmailMessage
import pyautogui as pyg
import time as t
import keyboard
import numpy as n
import random as rand
import win32api, win32con
import smtplib
import os

import movement
import mouse

#start of code

print("prepare.")
t.sleep(5) #sleep to begin
mouse.hold_down() #press mouse button

while True: #start loop
    if keyboard.is_pressed('z') == True: #stop code
        mouse.release()
        break
    mouse.hold_down()
    movement.move_left(40) #move left 
    movement.move_up(3) #move up 
    movement.move_right(40) #move right 
    movement.move_up(3) #move up 
    mouse.release()