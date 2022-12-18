import pyautogui as pag
import time

print('Starting in 5s...')
time.sleep(5)

while True:
    pag.keyDown('z')
    pag.keyUp('z')
    print('z')
    time.sleep(1)
    pag.keyDown('z')
    pag.keyUp('z')
    print('z')
    time.sleep(0.1)
    pag.keyDown('down')
    pag.keyUp('down')
    print('down')
    time.sleep(0.1)
    pag.keyDown('z')
    pag.keyUp('z')
    print('z')
    time.sleep(11)



