import cv2
import pyautogui
import time
import numpy as np
import initial
pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True

topleft = initial.initial()
#topleft = (435, 202)
#pixel = (2560,1600)
#kx = pixel[0]/1280
#ky = pixel[1]/800
#########
template = cv2.imread("../me.png",0)
#################
######mapSize####
import mss
import mss.tools


locateX = 0
locateY = 0

#####map#####
#region = {'top': 74, 'left': 18, 'width': 147, 'height': 98}
region = {'top': (topleft[1]+209-137), 'left': (270-263+topleft[0]) , 'width': 397-270, 'height': 265-209}

#############
def screenshot():
    with mss.mss() as sct:
        # The screen part to capture
        #region = {'top': (topleft[1]+125-51), 'left': (18+topleft[0]), 'width': (165-21), 'height': (218-125)}

        # Grab the data
        img = sct.grab(region)
        # Save to the picture file
        mss.tools.to_png(img.rgb, img.size, output='shot.png')
        return img

def getlocate():
    #im = pyautogui.screenshot(region=((18+topleft[0])*kx,(topleft[1]+125-51)*ky,(165-21)*kx,(218-125)*ky))
    img3 = screenshot()
    img3 = np.asarray(img3)
    #im.save('shot.png')
    #print('shot')
    ###############
    #img = cv2.imread('shot.png',0) # 0 读入灰度图
    #img3 = cv2.imread('shot.png',1) # 1 读入彩色图
    img = cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)

    img2 = img.copy()
    #template = cv2.imread("/Users/mac/Downloads/portral.png",0)

    #template = cv2.imread("/Users/mac/Downloads/me.png",0)

    #method = cv2.TM_CCOEFF
    method = cv2.TM_CCORR_NORMED
    #method = cv2.TM_CCOEFF_NORMED
    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    max_loc = [max_loc[0] * 1280/2560,max_loc[1] * 800/1600]

    x,y = max_loc
    #print('x,y:',x,y)
    global locateX , locateY
    if abs(locateX - x) > 5 or abs(locateY - y) >5:
        #print('wrong',x,y)
        pass
    locateX = x
    locateY = y
    return x,y


def main():
    while 1:
        #keyboard.wait('a')
        #cv2.waitKey(delay=500)
        #time.sleep(0.2)
        x,y = getlocate()
        print(x,y)
if __name__ == '__main__':
    main()
