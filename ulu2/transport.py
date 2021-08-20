import pyautogui
import time
import random
import time
from locate import getlocate  
pyautogui.PAUSE = 0.45
pyautogui.FAILSAFE = True
###macSet####
#############
topleft = (0,0)
pixel = (2560,1600)
kx = pixel[0]/1280
ky = pixel[1]/800
#################
######mapSize####

#x,y = getlocate()
xt,yt = 22,80
xt2 = 26#26
yplane = 28 + 2
#rand = 0.3 + 0.1*random.random()
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


def leftshift():
    time.sleep(0.05)
    pyautogui.hotkey('left','shift')
    time.sleep(0.05)
def rightshift():
    time.sleep(0.05)
    pyautogui.hotkey('right','shift')
    time.sleep(0.05)
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

def shift():
    pyautogui.hotkey('up','shift')#,interval = rand)
    time.sleep(0.5)
    pyautogui.hotkey('up','up','up')
    #time.sleep(0.6)
    #pyautogui.hotkey('up',interval = rand)
    pyautogui.hotkey('g',interval = rand)
    time.sleep(2)
    pyautogui.hotkey('left',interval = 0.5 + 0.1*random.random())
    pyautogui.hotkey('left','shift')#,interval = 0.3 + 0.1*random.random())

def Trans():
    time.sleep(0.15)# + 0.1*random.random())
    x,y = getlocate()
    print(x-xt)
    global rand
    rand = 0.2 + 0.1*random.random()
    pyautogui.PAUSE = rand
    while abs(x-xt) > 1:
        #rand = 0.5 + 0.1*random.random()
        #print(x-xt)
        if x < xt:
            pyautogui.keyDown('right')
            #pyautogui.hotkey('right',interval = 0.3)

            TT = time.time()
            while 1:
                x,y = getlocate()
                if abs(x-xt) < 2:
                    #time.sleep(0.05)
                    pyautogui.keyUp('right')
                    #time.sleep(0.05)
                    pyautogui.hotkey('up',interval = 0.1)
                    time.sleep(0.5)
                    #shift()
                    return
                if time.time() - TT > 3:
                    pyautogui.keyUp('right')
                    break
            '''
            x,y = getlocate()
            if abs(x-xt) < 2:
                time.sleep(0.05)
                pyautogui.keyUp('right')
                time.sleep(0.2)
                pyautogui.hotkey('up','shift',interval=0.2)
                Trans()
                #shift()
                return
            time.sleep(1.5)
            pyautogui.keyUp('right')
            return
            '''
        if x > xt:
            pyautogui.keyDown('left')
            #pyautogui.hotkey('left',interval = 0.3)
            TT = time.time()
            while 1:
                x,y = getlocate()
                if abs(x-xt) < 2:
                    #time.sleep(0.05)
                    pyautogui.keyUp('left')
                    #time.sleep(0.05)
                    pyautogui.hotkey('up',interval = 0.1)
                    time.sleep(0.5)
                    #shift()
                    return
                if time.time() - TT > 3:
                    pyautogui.keyUp('left')
                    break
            '''
            x,y = getlocate()
            if abs(x-xt) < 2:
                    time.sleep(0.05)
                    pyautogui.keyUp('left')
                    time.sleep(0.2)
                    pyautogui.hotkey('up','shift',interval=0.2)
                    Trans()
                    #shift()
                    return
            time.sleep(1.5)
            pyautogui.keyUp('left')
            return
            '''
        x,y = getlocate()
        print(x-xt)
    #time.sleep(0.05)
    pyautogui.hotkey('up',interval = 0.1)
    time.sleep(0.5)
    #shift()
    return

def walkToTrans():
    xt = xt2
    x,y = getlocate()
    print(x-xt)
    global rand
    rand = 0.4 + 0.1*random.random()
    pyautogui.PAUSE = rand
    while abs(x-xt+2) > 2:
        #rand = 0.5 + 0.1*random.random()
        if x < xt2:
            pyautogui.keyDown('right')
            #pyautogui.hotkey('right',interval = 0.3)
            TT = time.time()
            while 1:
                x,y = getlocate()
                if abs(x-xt2+2) < 3:
                    time.sleep(0.01)
                    pyautogui.keyUp('right')
                    time.sleep(0.05)
                    pyautogui.hotkey('up','shift',interval=0.2)
                    Trans()
                    #shift()
                    return
                if time.time() - TT > 2:
                    pyautogui.keyUp('right')
                    return
            time.sleep(1.5)
            pyautogui.keyUp('right')
            
        if x > xt:
            pyautogui.keyDown('left')
            #pyautogui.hotkey('left',interval = 0.3)
            TT = time.time()
            while 1:
                x,y = getlocate()
                if abs(x-xt2+2) < 3:
                    time.sleep(0.01)
                    pyautogui.keyUp('left')
                    time.sleep(0.05)
                    pyautogui.hotkey('up','shift',interval=0.2)
                    Trans()
                    #shift()
                    return
                if time.time() - TT > 2:
                    pyautogui.keyUp('left')
                    return
            time.sleep(1.5)
            pyautogui.keyUp('left')
        x,y = getlocate()
        print(x-xt)
    time.sleep(0.2)
    pyautogui.hotkey('up','shift',interval=0.2)
    Trans()
    #shift()
    return

def shiftToTrans():
    xt = xt2
    x,y = getlocate()
    print(x-xt)
    global rand
    #rand = 0.4 + 0.1*random.random()
    rand = 0.55
    pyautogui.PAUSE = rand

    TT = time.time()
    while abs(x-xt) > 10:
        #if time.time() - TT > 5:
        #    return
        #rand = 0.5 + 0.1*random.random()
        print(x-xt)
        if x < xt:
            #pyautogui.keyDown('right')
            rightTC()
            time.sleep(0.2)
            rightshift()
            #rightshift()
            #rightshift()
            time.sleep(0.2)
            #rightshift()
            rightshift()
            #rightshift()
            #leftTC()
            time.sleep(0.2)
            #leftshift()
            #leftshift()
            leftshift()
            time.sleep(0.55)
            #pyautogui.hotkey('right')
            #pyautogui.hotkey('right')
            '''
            while 1:
                x,y = getlocate()
                if abs(x-xt) < 3:
                    pyautogui.keyUp('right')
                    #time.sleep(0.5)
                    pyautogui.hotkey('up','shift')
                    Trans()
                    #shift()
                    return
            '''
        if x > xt:
            #pyautogui.keyDown('left')
            leftTC()
            time.sleep(0.2)
            leftshift()
            #leftshift()
            time.sleep(0.2)
            leftshift()
            #leftshift()
            #rightTC()
            time.sleep(0.2)
            leftshift()
            time.sleep(0.2)
            leftshift()
            #leftshift()
            
            time.sleep(0.55)
            '''
            while 1:
                x,y = getlocate()
                if abs(x-xt) < 3:
                    pyautogui.keyUp('left')
                    pyautogui.hotkey('up','shift')
                    Trans()
                    #shift()
                    return
            '''
        x,y = getlocate()
    #shift()
    return

def move():
    x,y = getlocate()
    if y > yt:
        shiftToTrans()
        #time.sleep(0.5)
        walkToTrans()
        #pyautogui.hotkey('v')
        #time.sleep(4)
        time.sleep(0.5)
    #pyautogui.hotkey('v')
    #time.sleep(3.15)
    #time.sleep(0.5)
    x,y = getlocate()
    #time.sleep(0.5)
    while y > yplane:
        pyautogui.hotkey('v')
        time.sleep(3.5)
        walkToTrans()
        x,y = getlocate()
        time.sleep(0.5)
    return
    
if __name__ == '__main__':
    x,y = getlocate()
    if y > yt:
        shiftToTrans()
        #time.sleep(0.5)
        walkToTrans()
        x,y = getlocate()

        #time.sleep(4)
        #pyautogui.hotkey('v')
        #time.sleep(4)
        #pyautogui.hotkey('v')
        #time.sleep(4)
    x,y = getlocate()
    time.sleep(0.5)
    while y > yplane:
        pyautogui.hotkey('v')
        time.sleep(3.5)
        walkToTrans()
        x,y = getlocate()
