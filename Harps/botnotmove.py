import pyautogui
import time
import random
from transport import move
from locate import getlocate
pyautogui.PAUSE = 0.45
pyautogui.FAILSAFE = True


###

###

###
Tstart = time.time()

global Timer
Timer = [Tstart,Tstart,Tstart,Tstart]#[genesis,g,v,d]

'''
T1 = 18 tap 41 | 70 88
T2 = 33 tap 50 | 29
                T3 = 40 - 44 tap 101 #73
T4 = 51 tap 15 50
                T5 = 55 tap |81 101
T6 = 70 tap
'''


xt = 56

'''
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
    return

def TCshiftright():
    TCTimer = time.time() - Timer[0]
    if TCTimer > 3.5:
        leftTC()
        Timer['TC'] = time.time()
    else:
        leftshift()
    return

def rightmove(xt,tolerance = 3):
        pyautogui.keyDown('right')
        #TT = time.time()
        x,y = getlocate()
        while x < xt - tolerance:
            x,y = getlocate()
            continue
        time.sleep(0.05)
        pyautogui.keyUp('right')
        time.sleep(0.05)
        return
        
def leftmove(xt,tolerance = 3):
        pyautogui.keyDown('left')
        #TT = time.time()
        x,y = getlocate()
        while x > xt + tolerance:
            x,y = getlocate()
            continue
        time.sleep(0.05)
        pyautogui.keyUp('left')
        time.sleep(0.05)
        return


def moveTo(xt,tolerance = 3):
    x,y = getlocate()
    while abs(x - xt) > tolerance:
        if x > xt:
            leftmove(xt)
        else:
            rightmove(xt)
        x,y = getlocate()
    return

def shiftTo(xt,tolerance = 10):

    x,y = getlocate()
    while abs(x - xt) > tolerance:
        
        if x < xt:
            TCshiftright()
        else:
            TCshiftleft()
        x,y = getlocate()
    return
        
'''

def buff(key=['g'],delay = 40,i=0):
    global bufftime
    timedelay = time.time() - Timer[i]
    print('timedelay'+str(key[0]),timedelay)
    time.sleep(0.1)
    if timedelay > delay:
        pyautogui.hotkey(*key)
        Timer[i] = time.time()
        time.sleep(1.5)
        return 1
    return 0

def genesis():
        Tnow = time.time()
        genesisTimer = time.time() - Timer[0]
        #print('genesisTimer:',genesisTimer)
        if genesisTimer > 5.5:
                Timer[0] = Tnow
                pyautogui.hotkey('v',interval = 0.5)
                print('new',Timer[0])
        return genesisTimer
'''
def genesis():
        Timer = genesisTimer()
        if Timer > 6:
                pyautogui.hotkey('v',interval = 0.5)
'''
def rightmove():
        pyautogui.keyDown('right')
        #pyautogui.hotkey('right',interval = 0.3)

        TT = time.time()
        #x,y = getlocate()
        while 1:
            x,y = getlocate()
            if x > xt - 3:
                time.sleep(0.05)
                pyautogui.keyUp('right')
                time.sleep(0.05)
                #pyautogui.hotkey('up',interval = 0.1)
                #time.sleep(0.5)
                #shift()
                return
            if time.time() - TT > 1.5:
                time.sleep(0.05)
                pyautogui.keyUp('right')
                time.sleep(0.05)
                return
        return
def leftmove():
        pyautogui.keyDown('left')
        #pyautogui.hotkey('right',interval = 0.3)

        TT = time.time()
        #x,y = getlocate()
        #while x > xt + 3:
        while 1:
            x,y = getlocate()
            if x < xt + 3:
                time.sleep(0.05)
                pyautogui.keyUp('left')
                time.sleep(0.05)
                #pyautogui.hotkey('up',interval = 0.1)
                #time.sleep(0.5)
                #shift()
                return
            if time.time() - TT > 1.5:
                time.sleep(0.05)
                pyautogui.keyUp('left')
                time.sleep(0.05)
                return
        x,y = getlocate()
        return

    
def addbuff():
    #addbuff()
    while Timer[0] < 4.0:
            pass
    print('checkbuff')
    if buff(['g'],50,1) == 1:
        buff(['g'],50,1)
        return
    if buff(['ctrl'],500,2) == 1:
        buff(['ctrl'],500,2)
        return
    if buff(['d','7'],300,3) == 1:
        buff(['d','7'],300,3)
        return

def loop():
    if Tier2:
        loopTap(x11)
        upTier()
    if Tier1:
        loopTap(x13)
        jumpDown()        
    if Tier3:
        left()
    if Tier4:
        loopTap(x21)
    return
def checkloop():
    loopTimer = time.time() - Timer[4]
    if loopTimer >120:
        loop()
        Timer[4] = time.time()
    return

def main():
        x ,y = getlocate()
        if abs(x-xt) > 2:
                x ,y = getlocate()
                if x < xt:
                        rightmove()
                        return
                else:
                        leftmove()
                        return
                return
        
            #Time = time.time()
            #if buff(['g'],50,1) == 1 :
        #checkloop()
        addbuff()
        genesis()

        time.sleep(0.1)
        return
'''
def bot():
        if x < 55 or x > 59:
                move()
        else:
                genesis()
'''





if __name__ == '__main__':
    time.sleep(1.5)
    pyautogui.hotkey('v',interval = 0.5)
    while 1:
        #time.sleep(0.2)
        main()
