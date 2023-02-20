import pyautogui as pyg
import time as t
import keyboard
import numpy as n
import random as rand
import win32api, win32con
import smtplib
import os

import responce
import commands

def detect():
    if pyg.pixel(734, 234)[1] != 252:
        if pyg.pixel(734, 175)[1] != 252:
            print("Off Island")
            t.sleep(5)
            commands.island_return()
        else:
            print("On Island!")
    else:
        print("On Island!")


#while True: #start loop
#    if keyboard.is_pressed('z') == True: #stop code
#        break
#    t.sleep(0.5)
#    detect()
#    if on_island == True:
#        print("true")
#    else:
#        print("false")

#t.sleep(2)
#detect()
#responce.printlist()
#t.sleep(10)
#detect()
#responce.printlist()
#t.sleep(5)
#responce.printlist()