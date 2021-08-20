import pyautogui
import time
pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True

time.sleep(2)
while 1:
    pyautogui.hotkey('left','shift','v')
