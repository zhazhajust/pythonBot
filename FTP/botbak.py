import pyautogui
import time
import random
from transport import move
from locate import getlocate
pyautogui.PAUSE = 0.45
pyautogui.FAILSAFE = True

###
rightX = 95
midX = 68
xt,yt = 22,80
yt1 = 65

rock1 = 70
rock2 = 80
###
global bufftime

bufftime = [time.time(),time.time(),time.time()]

###
def buff(key=['g'],delay = 20,i=0):
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
    time.sleep(0.003)
    pyautogui.keyDown('v')
    time.sleep(0.111)
    
    pyautogui.keyUp('left')
    time.sleep(0.011)
    pyautogui.keyUp('shift')
    time.sleep(0.004)
    pyautogui.keyUp('v')
    time.sleep(0.837)

def rightTC():
    time.sleep(0.037)
    pyautogui.keyDown('shift')
    time.sleep(0.002)
    pyautogui.keyDown('right')
    time.sleep(0.003)
    pyautogui.keyDown('v')
    time.sleep(0.111)
    
    pyautogui.keyUp('right')
    time.sleep(0.010)
    pyautogui.keyUp('shift')
    time.sleep(0.004)
    pyautogui.keyUp('v')
    time.sleep(0.837)
''' 
def topshift():
    #time.sleep(0.5)
    pyautogui.hotkey('left',interval=0.5)
    time.sleep(0.5)
    leftTC()
    #time.sleep(0.6)
    leftTC()
    leftTC()
    #time.sleep(0.6)
    leftTC()
    leftTC()
    #time.sleep(0.6)
    leftTC()
    leftTC()
    time.sleep(0.5)
    #pyautogui.hotkey('left','shift','v')

def downshift(x):
    if x > 46 and x < 86:
        time.sleep(0.05)
        pyautogui.hotkey('down','shift',interval = 0.1)
        time.sleep(0.05)
    else:
        time.sleep(0.05)
        pyautogui.hotkey('down','space',interval = 0.3)
        time.sleep(0.05)
rand = 0.5 + 0.1*random.random()
def main():
    #pyautogui.PAUSE = 0.5 + 0.1*random.random()
    x,y = getlocate()
    if x > rightX:
        '''
        pyautogui.hotkey('ctrl')
        time.sleep(1.5)
        pyautogui.hotkey('g')
        time.sleep(1.5)
        '''
        #time.sleep(1.5)
        topshift()
        '''
        pyautogui.hotkey('left',interval=0.5)
        
        pyautogui.hotkey('left','shift',interval=0.2)
        time.sleep(0.6)
        pyautogui.hotkey('left','shift',interval=0.2)
        '''
    #if y < yt and y > yt1:
    #    time.sleep(4)
    #    downshift()
    if y < rock2 and y > rock1:
        pyautogui.hotkey('right',interval = 0.5)
    if y > yt:
        #pyautogui.hotkey('d','7')
        buff(['d','7'],300,2)
        move()
        time.sleep(0.5)

        
        buff(['ctrl'],200,0)
        
        buff(['g'],1,1)
        #time.sleep(1.5)
        #buff(['d','7'],20,2)
        '''
        pyautogui.hotkey('ctrl')
        time.sleep(1.5)
        pyautogui.hotkey('g')
        time.sleep(1.5)
        '''
        time.sleep(1.5)
        topshift()

        

    if x > midX:
        leftTC()
        #leftTC()
        #leftTC()
        
        #time.sleep(0.6)
        leftTC()
        leftTC()
        #time.sleep(0.6)
        leftTC()
        leftTC()
        #time.sleep(0.6)
        #rightTC()
        rightTC()
        rightTC()
        time.sleep(0.5)
        #time.sleep(0.6)
        #time.sleep(0.5)
        
        #rightshift()
    if x < midX:
        rightTC()
        #rightTC()
        #rightTC()
        #time.sleep(0.6)
        rightTC()
        #time.sleep(0.6)
        rightTC()
        #time.sleep(0.6)
        #time.sleep(0.6)
        rightTC()
        #time.sleep(0.6)
        rightTC()
        #time.sleep(0.6)
        #leftTC()
        leftTC()
        leftTC()
        time.sleep(0.5)
        #time.sleep(0.6)
        #time.sleep(0.5)
        #leftshift()
        #rightshift()
        #rightshift()
    if y < yt:
        #time.sleep(0.5)
        downshift(x)
        time.sleep(0.5)
        return
    if y > yt:
        buff(['d','7'],500,2)
        move()
        time.sleep(0.5)
    '''
        leftTC()
        leftshift()
        return
    if abs(x - xt) < 10:
        transport()
    '''
if __name__ == '__main__':
    time.sleep(2)
    while 1:
        #time.sleep(0.2)
        main()
