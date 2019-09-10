from pynput.keyboard import Key, Controller
from time import sleep
keyb = Controller()
import pyautogui
import keyboard
while True:
    try:
        i = 0
        if keyboard.is_pressed('c'):
            while i!=1:
                if keyboard.is_pressed('x'):
                    i=1
                pyautogui.click(button = 'right')
           
        if keyboard.is_pressed('z'):
            while i!=1:
                if keyboard.is_pressed('x'):
                    i=1
                pyautogui.click(button = 'left')
    except:
        pass
       
