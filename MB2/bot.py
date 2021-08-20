import pyautogui
import time
import random
from transport import move
from locate import getlocate
pyautogui.PAUSE = 0.45
pyautogui.FAILSAFE = True

###
rightX = 95
midX = 60
xt,yt = 75,80
yt1 = 65

rock1 = 70
rock2 = 80
###
global bufftime

bufftime = [time.time(),time.time(),time.time()]

###

def leftTC():
    #pyautogui.keyDown('left')
    time.sleep(0.05)
    pyautogui.hotkey('left','shift','v')    
    time.sleep(0.05)
    #pyautogui.keyUp('left')


def rightTC():
    #pyautogui.keyDown('right')
    time.sleep(0.05)
    pyautogui.hotkey('right','shift','v')
    time.sleep(0.05)
    #pyautogui.keyUp('right')

def leftshift():
    time.sleep(0.05)
    pyautogui.hotkey('left','shift')
    time.sleep(0.05)
def rightshift():
    time.sleep(0.05)
    pyautogui.hotkey('right','shift')
    time.sleep(0.05)

def TCshiftleft():
    TCTimer = time.time() - Timer[0]
    if TCTimer > 3.5:
        leftTC()
        Timer['TC'] = time.time()
    else:
        leftshift()

def TCshiftright():
    TCTimer = time.time() - Timer[0]
    if TCTimer > 3.5:
        leftTC()
        Timer['TC'] = time.time()
    else:
        leftshift()


def moveTo(xt):
    if x > xt:
        left()

def shiftTo():
    while 1:
        x,y = getlocate()
        if x < xt:
            TCshiftright()
        else:
            TCshiftleft()
        


def leftLoop():
        leftTC()
        #leftTC()
        #leftTC()
                
        time.sleep(0.2)
        leftshift()
        #leftshift()
        time.sleep(0.2)
        #leftshift()
        leftshift()
        time.sleep(0.2)
        #rightTC()
        #rightshift()
        rightshift()
        time.sleep(0.55)
        #time.sleep(0.6)
        #time.sleep(0.5)
                
        #rightshift()

def rightLoop():
        rightTC()
        #rightTC()
        #rightTC()
        time.sleep(0.2)
        rightshift()
        time.sleep(0.2)
        #rightshift()
        #time.sleep(0.55)
        #time.sleep(0.6)
        #rightshift()
        #time.sleep(0.6)
        rightshift()
        time.sleep(0.2)
        #leftTC()
        #leftshift()
        leftshift()
        time.sleep(0.55)
        #time.sleep(0.6)
        #time.sleep(0.5)
        #leftshift()
        #rightshift()
        #rightshift()

def buff(key=['g'],delay = 40,i=0):
    global bufftime
    timedelay = time.time() - bufftime[i]
    print('timedelay',timedelay)
    time.sleep(0.1)
    if timedelay > delay:
        pyautogui.hotkey(*key)
        bufftime[i] = time.time()
        time.sleep(1.5)
    return

def leftTC():
    #pyautogui.keyDown('left')
    time.sleep(0.05)
    pyautogui.hotkey('left','shift','v')    
    time.sleep(0.05)
    #pyautogui.keyUp('left')


def rightTC():
    #pyautogui.keyDown('right')
    time.sleep(0.05)
    pyautogui.hotkey('right','shift','v')
    time.sleep(0.05)
    #pyautogui.keyUp('right')
def leftshift():
    time.sleep(0.05)
    pyautogui.hotkey('left','shift')
    time.sleep(0.05)
def rightshift():
    time.sleep(0.05)
    pyautogui.hotkey('right','shift')
    time.sleep(0.05)
'''

def leftTC():
    time.sleep(0.037)
    pyautogui.keyDown('shift')
    time.sleep(0.002)
    pyautogui.keyDown('left')
    time.sleep(0.011)
    pyautogui.keyDown('v')
    time.sleep(0.111)
    
    pyautogui.keyUp('left')
    time.sleep(0.031)
    pyautogui.keyUp('shift')
    time.sleep(0.004)
    pyautogui.keyUp('v')
    time.sleep(0.637)

def rightTC():
    time.sleep(0.037)
    pyautogui.keyDown('shift')
    time.sleep(0.002)
    pyautogui.keyDown('right')
    time.sleep(0.011)
    pyautogui.keyDown('v')
    time.sleep(0.111)
    
    pyautogui.keyUp('right')
    time.sleep(0.031)
    pyautogui.keyUp('shift')
    time.sleep(0.004)
    pyautogui.keyUp('v')
    time.sleep(0.637)
'''
def topshift():
    #time.sleep(0.5)
    pyautogui.hotkey('left',interval=0.6)
    time.sleep(0.5)
    leftTC()
    time.sleep(0.55)
    leftshift()
    #time.sleep(0.6)
    leftshift()
    #time.sleep(0.6)
    leftshift()
    
    leftshift()
    time.sleep(0.6)
    #leftshift()
    #leftshift()
    #time.sleep(0.5)
    #pyautogui.hotkey('left','shift','v')

def downshift(x):
    if x > 46 and x < 86:
        time.sleep(0.05)
        #pyautogui.hotkey('down','shift',interval = 0.25)
        pyautogui.keyDown('shift')
        time.sleep(0.02)
        pyautogui.keyDown('down')
        time.sleep(0.05)
        pyautogui.keyUp('shift')
        time.sleep(0.015)
        pyautogui.keyUp('down')
        time.sleep(0.004)
        time.sleep(0.75)
    else:
        time.sleep(0.05)
        #pyautogui.hotkey('down','space',interval = 0.25)
        pyautogui.keyDown('down')
        time.sleep(0.011)
        pyautogui.keyDown('space')
        time.sleep(0.05)
        
        pyautogui.keyUp('down')
        time.sleep(0.031)
        pyautogui.keyUp('space')
        time.sleep(0.004)
        time.sleep(0.75)
rand = 0.5 + 0.1*random.random()
def main():
    #pyautogui.PAUSE = 0.5 + 0.1*random.random()
    x,y = getlocate()

    if abs(x - xt) < 10:
        buff(['ctrl'],150,0)
        
        buff(['g'],60,1)
        #time.sleep(1.5)
        buff(['d','7'],200,2)
        
    if x > midX - 1:
        leftshift()
        #leftshift()
        time.sleep(0.2)
        leftshift()
        time.sleep(0.2)
        leftshift()
        time.sleep(0.55)
 
        #leftLoop()
        leftLoop()
    if x < midX:
        rightshift()
        time.sleep(0.2)
        rightshift()
        time.sleep(0.2)
        #time.sleep(0.6)
        rightshift()
        time.sleep(0.55)
        #rightLoop()
        rightLoop()
    


if __name__ == '__main__':
    time.sleep(2)
    while 1:
        #time.sleep(0.2)
        main()
