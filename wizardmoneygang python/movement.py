import pyautogui as pyg
import time as t
import keyboard
import numpy as n
import random as rand
import win32api, win32con
import smtplib
import os

import mouse
import values
import responce
import screendetector
import commands

#Base Sneaking Speed:           4.3 Blocks
#Base Walking Speed:            1.3 Blocks
#Base Sprinting Speed:          5.6 Blocks

#Upgraded Sneaking Speed:       4.429 Blocks
#Upgraded Walking Speed:        1.339 Blocks
#Upgraded Sprinting Speed:      5.767 Blocks

Speed = 4.429
Forward_Blocks = 6
Sideways_Blocks = 160

def move_up():
    screendetector.detect()
    select_hoe()
    print("walking forward...")
    pyg.keyDown('w')
    t.sleep(Forward_Blocks / Speed)
    pyg.keyUp('w')
    commands.setspawn()
    screendetector.detect()

def move_left():
    screendetector.detect()
    select_hoe()
    print("walking to the left...")
    mouse.hold_down()
    pyg.keyDown('a')
    t.sleep(Sideways_Blocks / Speed)
    pyg.keyUp('a')
    mouse.release()
    values.row_count += 1
    responce.printlist()
    screendetector.detect()

def move_right():
    screendetector.detect()
    select_hoe()
    mouse.hold_down()
    print("walking to the right...")
    pyg.keyDown('d')
    t.sleep(Sideways_Blocks / Speed)
    pyg.keyUp('d')
    mouse.release()
    values.row_count += 1
    responce.printlist()
    screendetector.detect()

def select_hoe():
    pyg.press('1')