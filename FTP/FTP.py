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
xt,yt = 22,(80)
yt1 = 65

rock1 = 70
rock2 = 80
###
global bufftime

Timer = {'TC':Tstart,'gen':Tstart,'buff0':Tstart,'buff1':Tstart,'buff2':Tstart,'buff3':Tstart,'loop':Tstart}

bufftime = [time.time(),time.time(),time.time()]

###
tap = [[70,28],[49,43],[77,54],[53,69]]

###

def checktap(x,y):
        for x1,y1 in tap:
             if y == y1 and abs(x-x1)<3:
                     pyautogui.hotkey('right',interval = 1)
                     

                
def leftLoop():
        leftTC()
        #leftTC()
        #leftTC()
                
        time.sleep(0.2)
        leftshift()
        #leftshift()
        time.sleep(0.2)
        leftshift()
        time.sleep(0.2)
        #leftshift()
        #time.sleep(0.2)
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
        rightshift()
        time.sleep(0.2)
        #time.sleep(0.6)
        #rightshift()
        #time.sleep(0.6)
        #rightshift()
        #time.sleep(0.2)
        #leftTC()
        #leftshift()
        leftshift()
        time.sleep(0.55)
        #time.sleep(0.6)
        #time.sleep(0.5)
        #leftshift()
        #rightshift()
        #rightshift()


'''
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
'''

def buff(key=['g'],delay = 40,i=0):
    
    TCTimer = time.time() - Timer['gen']
    print('checkbuff')
    #while TCTimer < 3.5:
    #    TCTimer = time.time() - Timer['gen']
    #    continue
    
    #print('checkbuff')
    global bufftime
    timedelay = time.time() - Timer['buff'+str(i)]
    print('timedelay'+str(key[0]),timedelay)
    time.sleep(0.1)
    if timedelay > delay:
        pyautogui.hotkey(*key)
        Timer['buff'+str(i)] = time.time()
        time.sleep(1.5)
        return 1
    return 0

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
    TCTimer = time.time() - Timer['TC']
    if TCTimer > 3.5:
        leftTC()
        Timer['TC'] = time.time()
    else:
        leftshift()
    return

def TCshiftright():
    TCTimer = time.time() - Timer['TC']
    if TCTimer > 3.5:
        rightTC()
        Timer['TC'] = time.time()
    else:
        rightshift()
    return

def rightmove(xt,tolerance = 3):
        pyautogui.keyDown('right')
        #TT = time.time()
        x,y = getlocate()
        while x < xt - tolerance:
            x,y = getlocate()
            continue
        #time.sleep(0.01)
        pyautogui.keyUp('right')
        #time.sleep(0.01)
        return
        
def leftmove(xt,tolerance = 3):
        pyautogui.keyDown('left')
        #TT = time.time()
        x,y = getlocate()
        while x > xt + tolerance:
            x,y = getlocate()
            continue
        #time.sleep(0.01)
        pyautogui.keyUp('left')
        #time.sleep(0.01)
        return


def moveTo(xt,tolerance = 4):
    x,y = getlocate()
    while abs(x - xt) > tolerance:
        if x > xt:
            leftmove(xt)
        else:
            rightmove(xt)
        x,y = getlocate()
    #time.sleep(0.01)
    return

def shiftTo(xt,tolerance = 10):

    x,y = getlocate()
    while abs(x - xt) > tolerance:
        #x,y = getlocate()
        if x < xt:
            TCshiftright()
        else:
            TCshiftleft()
        x,y = getlocate()
    #time.sleep(0.01)
    return

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
    rand = 0.5 + 0.1*random.random()

    pyautogui.hotkey('left',interval=rand)


    #time.sleep(1.5)
    #time.sleep(0.5)
    
    pyautogui.hotkey('v',interval=0.6)
    time.sleep(3.6)

    leftTC()
    time.sleep(0.2)
    leftshift()
    time.sleep(0.2)
    leftshift()
    time.sleep(0.2)
    leftshift()
    time.sleep(0.05)
    shiftTo(65)
    x,y = getlocate()
    #time.sleep(0.5)
    checktap(x,y)
    downshift(x)
    #leftshift()
    #leftshift()
    
    #leftshift()
    #leftshift()
    time.sleep(0.85)

    #leftLoop()
    #buff(['g'],1,1)
    #leftshift()
    #leftshift()
    #time.sleep(0.5)
    #pyautogui.hotkey('left','shift','v')

def downshift(x):
    if x > 46 and x < 86:
        time.sleep(0.05)
        pyautogui.hotkey('down','shift',interval = 0.25)
        time.sleep(0.4)
    else:
        time.sleep(0.05)
        pyautogui.hotkey('down','space',interval = 0.25)
        time.sleep(0.4)
'''
def downshift(x):
    if x > 46 and x < 86:
        time.sleep(0.05)
        #pyautogui.hotkey('down','shift',interval = 0.25)
        pyautogui.keyDown('down')
        time.sleep(0.02)
        pyautogui.keyDown('shift')
        time.sleep(0.114)
        pyautogui.keyUp('down')
        time.sleep(0.015)
        pyautogui.keyUp('shift')
        time.sleep(0.004)
        time.sleep(0.75)
    else:
        time.sleep(0.05)
        #pyautogui.hotkey('down','space',interval = 0.25)
        pyautogui.keyDown('down')
        time.sleep(0.051)
        pyautogui.keyDown('space')
        time.sleep(0.115)
        
        pyautogui.keyUp('down')
        time.sleep(0.031)
        pyautogui.keyUp('space')
        time.sleep(0.004)
        time.sleep(0.75)
'''       
rand = 0.5 + 0.1*random.random()
def main():
    #pyautogui.PAUSE = 0.5 + 0.1*random.random()
    x,y = getlocate()

    #checktap(x,y)
    if x > rightX: #and y == 28:
        '''
        pyautogui.hotkey('ctrl')
        time.sleep(1.5)
        pyautogui.hotkey('g')
        time.sleep(1.5)
        '''

        topshift()
        #time.sleep(1.5)

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

        buff(['ctrl'],150,0)
        
        buff(['g'],1,1)
        time.sleep(0.5)

        #time.sleep(1.5)
        #buff(['d','7'],20,2)
        '''
        pyautogui.hotkey('ctrl')
        time.sleep(1.5)
        pyautogui.hotkey('g')
        time.sleep(1.5)
        '''
        time.sleep(0.5)
        topshift()

        

    if x > midX:
        leftLoop()
    if x < midX:
        rightLoop()
    
    if y < yt:
        x,y = getlocate()
        #time.sleep(0.5)
        

        checktap(x,y)
        downshift(x)
        #time.sleep(0.55)
        return
    if y > yt:
        buff(['d','7'],500,2)
        move()
        time.sleep(0.55)
    '''
        leftTC()
        leftshift()
        return
    if abs(x - xt) < 10:
        transport()
    '''
    time.sleep(0.1)
if __name__ == '__main__':
    time.sleep(2)
    while 1:
        #time.sleep(0.2)
        main()
