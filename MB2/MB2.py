import pyautogui
import time
import random
from transport import move
from locate import getlocate
#pyautogui.PAUSE = 0.05
pyautogui.PAUSE = 0.45
pyautogui.FAILSAFE = True


###

###
###

###

###
Tstart = time.time()

global Timer
#Timer = [Tstart,Tstart,Tstart,Tstart]#[genesis,g,v,d]
Timer = {'TC':Tstart,'gen':Tstart,'buff0':Tstart,'buff1':Tstart,'buff2':Tstart,'buff3':Tstart,'loop':Tstart}

'''
T1 = 18 tap 41 | 70 88
T2 = 33 tap 50 | 29
                T3 = 40 - 44 tap 101 #73
T4 = 51 tap 15 50
                T5 = 55 tap |81 101
T6 = 70 tap
'''
###
rightX = 95
midX = 60
xt,yt = 75,80
yt1 = 65

rock1 = 70
rock2 = 80
###

#xt = 56


def leftTC():
    
    #pyautogui.keyDown('left')
    time.sleep(0.05)
    pyautogui.hotkey('left','shift','v')#,interval = 0.45)    
    time.sleep(0.05)
    #pyautogui.keyUp('left')
    '''
    pyautogui.keyDown('left')
    time.sleep(0.01)
    pyautogui.keyDown('shift')
    time.sleep(0.01)
    pyautogui.keyDown('v')
    time.sleep(0.01)

    pyautogui.keyUp('shift')
    time.sleep(0.01)
    pyautogui.keyUp('v')
    time.sleep(0.01)
    pyautogui.keyUp('left')
    time.sleep(0.01)
    
    time.sleep(0.5)
    '''
def rightTC():
    #pyautogui.keyDown('right')
    time.sleep(0.05)
    pyautogui.hotkey('right','shift','v')#,interval = 0.45)
    time.sleep(0.05)
    #time.sleep(0.55)
    #pyautogui.keyUp('right')

def leftshift():
    
    time.sleep(0.05)
    pyautogui.hotkey('left','shift')#,interval = 0.45)
    time.sleep(0.05)
    #time.sleep(0.55)
    '''
    pyautogui.keyDown('left')
    time.sleep(0.01)
    pyautogui.keyDown('shift')
    time.sleep(0.1)
    pyautogui.keyUp('shift')
    time.sleep(0.01)
    pyautogui.keyUp('left')
    time.sleep(0.05)

    time.sleep(0.5)
    '''
def rightshift():
    time.sleep(0.05)
    pyautogui.hotkey('right','shift')#,interval = 0.45)
    time.sleep(0.05)
    #time.sleep(0.55)

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


def moveTo(xt,tolerance = 3):
    x,y = getlocate()
    while abs(x - xt) > tolerance:
        if x > xt:
            leftmove(xt,tolerance)
        else:
            rightmove(xt,tolerance)
        x,y = getlocate()
    return

def shiftTo(xt,tolerance = 10):

    x,y = getlocate()
    while abs(x - xt) > tolerance:
        #x,y = getlocate()
        if abs(x-51) < 10:
            addbuff()
        
        if x < xt:
            TCshiftright()
        else:
            TCshiftleft()
        x,y = getlocate()
    return
        
def jump(xp,yp1,yp2):
    while 1:
        x , y = getlocate()
        #pyautogui.hotkey('space','up',interval = 0.15)
        if x < xp:
            pyautogui.keyDown('right')
        if x > xp:
            pyautogui.keyDown('left')
        pyautogui.keyDown('space')
        time.sleep(0.01)
        pyautogui.keyDown('up')
        time.sleep(0.5)
        pyautogui.keyUp('up')
        time.sleep(0.05)
        pyautogui.keyUp('space')
        time.sleep(0.05)
        
        pyautogui.keyDown('up')
        time.sleep(0.05)
        pyautogui.keyUp('left')
        pyautogui.keyUp('right')
        time.sleep(0.3)
        x , y = getlocate()
        if x == xp and y < yp1:
            
            break
        else:
            pyautogui.keyUp('up')
            moveTo(xp)
            
            continue
    while 1:
        time.sleep(0.01)
        x , y = getlocate()
        if y == yp2:
            time.sleep(0.2)
            pyautogui.keyUp('up')
            time.sleep(0.01)
            break

    print('finish jump'+str(yp2))
    return

def buff(key=['g'],delay = 40,i=0):
    TCTimer = time.time() - Timer['TC']
    print('checkbuff')

    #time.sleep(3.5)
    
    global bufftime
    timedelay = time.time() - Timer['buff'+str(i)]
    print('timedelay'+str(key[0]),timedelay)
    time.sleep(0.1)
    if timedelay > delay:
        while TCTimer < 3.5:
            TCTimer = time.time() - Timer['TC']
            continue
        pyautogui.hotkey(*key)
        Timer['buff'+str(i)] = time.time()
        time.sleep(1.5)
        return 1
    return 0

def genesis():
        Tnow = time.time()
        genesisTimer = time.time() - Timer['gen']
        #print('genesisTimer:',genesisTimer)
        if genesisTimer > 5.5:
                Timer['gen'] = Tnow
                pyautogui.hotkey('v',interval = 0.5)
                print('new',Timer['gen'])
        return genesisTimer



def addbuff():
    #addbuff()
    '''
    print('checkbuff')
    if buff(['g'],10,1) == 1:
        shiftTo(75)
        while Timer['gen'] < 4.0:
            pass
        buff(['g'],0,1)
        return
    if buff(['ctrl'],500,2) == 1:
        shiftTo(75)
        while Timer['gen'] < 4.0:
            pass
        buff(['ctrl'],0,2)
        return
    if buff(['d','7'],300,3) == 1:
        shiftTo(75)
        while Timer['gen'] < 4.0:
            pass
        buff(['d','7'],0,3)
        return
    '''
    '''
    TCTimer = time.time() - Timer['TC']
    print('checkbuff')
    while TCTimer < 3.5:
        TCTimer = time.time() - Timer['TC']
        continue
    #time.sleep(3.5)
    '''
    if buff(['g'],50,1) == 1:
        #buff(['g'],0,1)
        return
    if buff(['ctrl'],450,2) == 1:
        #buff(['ctrl'],0,2)
        return
    if buff(['d','7'],500,3) == 1:
        #buff(['d','7'],0,3)
        return
def loop():
    shiftTo(41)
    moveTo(41)
    jump(41,33,18)
    shiftTo(85)
    moveTo(91,tolerance = 1)
    pyautogui.hotkey('down','space',interval = 0.3)
    shiftTo(54)
    moveTo(40)
    shiftTo(29)
    moveTo(29)
    
    jump(29,51,33)#,18
    '''
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
    '''
    return
def checkloop(looptime=120):
    loopTimer = time.time() - Timer['loop']
    if loopTimer > looptime:
        loop()
        Timer['loop'] = time.time()
    return

def main():
    x ,y = getlocate()
    #addbuff()
    '''
    if abs(x - xt) < 10:
        buff(['ctrl'],150,0)
        
        buff(['g'],60,1)
        #time.sleep(1.5)
        buff(['d','7'],200,2)
    '''
    if x > midX - 1:
        shiftTo(25)


    if x < midX:
        shiftTo(95)

    return

def testjump():
    #shiftTo(41)
    #moveTo(41)
    #jump(41,33,18)
    while 1:
        leftTC()
        leftshift()
        leftshift()
        #leftshift()

if __name__ == '__main__':
    time.sleep(1.5)
    pyautogui.hotkey('v',interval = 0.5)
    '''
    while 1:
        #time.sleep(0.2)
        #main()
        #testjump()
        loop()
    '''
    while 1:
        main()
