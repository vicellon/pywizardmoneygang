import pyautogui as pyg
import time as t
import keyboard
import numpy as n
import random as rand
import win32api, win32con
import smtplib
import os

import movement
import screendetector
import commands
import mouse
import values

def clear():
    os.system('cls')

def printlist():
    clear()
    print(f"Rows Farmed: {values.row_count}")
    print(f"Times Returned To Island: {values.times_returned}")