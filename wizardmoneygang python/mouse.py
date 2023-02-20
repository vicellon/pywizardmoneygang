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

def click():
    print("click")
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    t.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)
    t.sleep(0.01)

def double_click():
    print("double click")
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    t.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)
    t.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    t.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)
    t.sleep(0.01)

def hold_down():
    pyg.mouseDown()

def release():
    pyg.mouseUp()