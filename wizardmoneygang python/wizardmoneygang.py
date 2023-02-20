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
import responce
import screendetector

def main():
    screendetector.detect()
    movement.move_left()      #move left 
    movement.move_up()         #move up 
    movement.move_right()     #move right 
    movement.move_up()         #move up 

def prepare():
    print("starting code...")
    t.sleep(10)

#start of code
prepare()

while True:                     #start loop
    main()    