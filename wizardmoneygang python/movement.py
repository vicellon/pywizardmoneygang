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

def move_up(time):
    pyg.keyDown('w')
    t.sleep(time)
    pyg.keyUp('w')

def move_left(time):
    pyg.keyDown('a')
    t.sleep(time)
    pyg.keyUp('a')

def move_right(time):
    pyg.keyDown('d')
    t.sleep(time)
    pyg.keyUp('d')