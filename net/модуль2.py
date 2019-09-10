from pynput.keyboard import Key, Controller
import keyboard
from time import sleep
keyb = Controller()
i = 0
while True:
    
    if keyboard.is_pressed('a'):
        while i != 1:
                if keyboard.is_pressed('s'):
                    i = 1
                keyb.press('е')
                keyb.press('б')
                keyb.press('а')
                keyb.press('н')
                keyb.press('ы')
                keyb.press('й')
                keyb.press(' ')
                keyb.press('д')
                keyb.press('а')
                keyb.press('у')
                keyb.press('н')
                sleep(1)
                keyb.press(Key.enter) 
            


