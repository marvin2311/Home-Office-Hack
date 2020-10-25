#import required modules
import pyautogui
import time

pyautogui.FAILSAFE = False

#sleep for 10 sec
time.sleep(10)

#infinity loop (will run all day long)
while True:

    #move the mouse from the upper left corner in the direction of the lower right corner
    for i in range(0,100):
        pyautogui.moveTo(i*10,i*5)

    #for i in range(0,3):
    #    pyautogui.press('left')
    #    pyautogui.press('up')
    #    pyautogui.press('right')
    #    pyautogui.press('down')

    #sleep for 10 sec
    time.sleep(10)
