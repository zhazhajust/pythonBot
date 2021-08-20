import pyautogui
import time
import random
from transport import move
from locate import getlocate
pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True


###

###

###
Tstart = time.time()

global Timer
#Timer = [Tstart,Tstart,Tstart,Tstart]#[genesis,g,v,d]
Timer = {'TC':Tstart,'gen':Tstart,'buff0':Tstart,'buff1':Tstart,'buff2':Tstart,'buff3':Tstart,'buff4':Tstart,'loop':Tstart}

'''
T1 = 18 tap 41 | 70 88
T2 = 33 tap 50 | 29
                T3 = 40 - 44 tap 101 #73
T4 = 51 tap 15 50
                T5 = 55 tap |81 101
T6 = 70 tap
'''


xt = 56


def leftTC():
    pyautogui.PAUSE = 0.45
    #pyautogui.keyDown('left')
    time.sleep(0.05)
    pyautogui.hotkey('left','shift','v')#,interval = 0.45)    
    time.sleep(0.05)
    pyautogui.PAUSE = 0.05
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
    pyautogui.PAUSE = 0.45
    #pyautogui.keyDown('right')
    time.sleep(0.05)
    pyautogui.hotkey('right','shift','v')#,interval = 0.45)
    time.sleep(0.05)
    pyautogui.PAUSE = 0.05
    #time.sleep(0.55)
    #pyautogui.keyUp('right')

def leftshift():
    
    time.sleep(0.05)
    pyautogui.hotkey('left','shift',interval = 0.3)
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
    pyautogui.hotkey('right','shift',interval = 0.3)
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

def rightmove(xt,tolerance = 1):
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
        
def leftmove(xt,tolerance = 1):
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
        
def jump(xp,yp1,yp2):
    while 1:
        x , y = getlocate()
        #pyautogui.hotkey('space','up',interval = 0.15)
        if x < xp - 1:
            pyautogui.keyDown('right')
        if x > xp + 1:
            pyautogui.keyDown('left')

        pyautogui.keyDown('up')
        time.sleep(0.01)

        pyautogui.keyDown('space')

        if x == xp - 1:
            pyautogui.keyDown('right')
        if x == xp + 1:
            pyautogui.keyDown('left')

        time.sleep(0.4)



        if y > yp1 + 1:
            pyautogui.keyUp('up')
            pyautogui.keyUp('space')
            
            moveTo(xp,1)
            #return
        time.sleep(0.1)
        pyautogui.keyUp('up')
        time.sleep(0.05)
        pyautogui.keyUp('space')
        time.sleep(0.05)
        
        pyautogui.keyDown('up')
        time.sleep(0.05)
        pyautogui.keyUp('left')
        pyautogui.keyUp('right')
        time.sleep(0.5)
        x , y = getlocate()
        if x == xp and y < yp1:
            break
        else:
            pyautogui.keyUp('up')
            pyautogui.keyUp('space')
            if abs(x - xp) > 4:
                moveTo(xp)
            #return
            continue
    while 1:
        time.sleep(0.01)
        x , y = getlocate()
        if y == yp2:
            time.sleep(0.20)
            pyautogui.keyUp('up')
            time.sleep(0.01)
            break


    print('finish jump'+str(yp2))
    return

def leftjump():

    pyautogui.keyDown('left')
    pyautogui.keyDown('space')
    time.sleep(0.01)
    pyautogui.keyDown('up')
    time.sleep(0.5)
    pyautogui.keyUp('up')
    time.sleep(0.05)
    pyautogui.keyUp('space')
    time.sleep(0.01)
    
    pyautogui.keyDown('up')
    time.sleep(0.01)
    pyautogui.keyUp('left')
    time.sleep(0.01)
    pyautogui.keyUp('up')

    time.sleep(0.4)
    
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
    pyautogui.keyUp('up')

def buff(key=['g'],delay = 40,i=0):

    TCTimer = time.time() - Timer['gen']
    print('checkbuff')

    
    #print('checkbuff')
    global bufftime
    timedelay = time.time() - Timer['buff'+str(i)]
    print('timedelay'+str(key[0]),timedelay)
    time.sleep(0.1)
    if timedelay > delay:
        while TCTimer < 3.5:
            TCTimer = time.time() - Timer['gen']
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
        if genesisTimer > 5.0:
                Timer['gen'] = Tnow
                pyautogui.hotkey('v',interval = 0.5)
                print('new',Timer['gen'])
        return genesisTimer



def addbuff():
    #addbuff()

    Tnow = time.time()
    buffTimer = time.time() - Timer['buff0']
    #print('genesisTimer:',genesisTimer)
    if buffTimer < 40:
        return
    else:
        Timer['buff0'] = Tnow
        
    #while Timer['gen'] < 3.8:
    #    continue
    print('checkbuff')

    if buff(['ctrl'],400,2) == 1:
        pass
        #buff(['ctrl'],0,2)
        #return
    if buff(['g'],40,1) == 1:
        time.sleep(0.5)
        pass
        #buff(['g'],0,1)
        #return
    if buff(['d','7'],450,3) == 1:
        time.sleep(0.5)
        pass

    if buff(['-'],150,4) == 1:
        pass
        #buff(['d','7'],0,3)
        #return
    return

def loop():
    while Timer['gen'] < 3.5:
        continue
    shiftTo(37)
    moveTo(41,1)
    x ,y = getlocate()
    while y != 38:
        #moveTo(37)
        jump(37,57,38)
        time.sleep(0.2)
        x ,y = getlocate()

    shiftTo(7)
    moveTo(2)

    shiftTo(105)
    moveTo(110,2)
    
    #moveTo(82,tolerance = 2)
    while y == 38:
        pyautogui.hotkey('down','space',interval = 0.3)
        time.sleep(0.2)
        x ,y = getlocate()
    #shiftTo(60)
    #moveTo(54,1)

    #leftjump()
    
    #moveTo(40,tolerance = 2)
    #shiftTo(29+4)
    #moveTo(29+4,1)
    #x ,y = getlocate()
    #while y!= 33:
    #    jump(29,51,33)#,18
    #    time.sleep(0.1)
    #    x ,y = getlocate()
    shiftTo(7)
    moveTo(2,2)

    shiftTo(45)
    moveTo(41)
    addbuff()
    #addbuff()
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
        
        addbuff()
        checkloop(130)
        #genesis()


        if x <= xt:
            shiftTo(105)

        if x > xt:
            shiftTo(15)

            #Time = time.time()
            #if buff(['g'],50,1) == 1 :
            
        time.sleep(0.1)
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
    #pyautogui.hotkey('v',interval = 0.5)
    '''
    while 1:
        #time.sleep(0.2)
        #main()
        testjump()
        #loop()
    '''
    #testjump()
    while 1:
        main()


