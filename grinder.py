import pyautogui as pag
import time

#pag.PAUSE = 1

time.sleep(5)

# Start with spamming z to run from fight and retrigger, continue for 6s
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



