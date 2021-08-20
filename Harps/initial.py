# 导入模块 cv2匹配算法 plt 显示图片
import cv2
from matplotlib import pyplot as plt
import mss
# 读入图片 big1.png是背景大图; small.png是需要寻找的小图（格式.jpg .png都行）
#x,y = 

region = {'top':0, 'left': 0, 'width': 1280, 'height': 800}
def screenshot():
    with mss.mss() as sct:
        # The screen part to capture
        #region = {'top': (topleft[1]+125-51), 'left': (18+topleft[0]), 'width': (165-21), 'height': (218-125)}

        # Grab the data
        img = sct.grab(region)
        # Save to the picture file
        mss.tools.to_png(img.rgb, img.size, output='VM.png')
        return img


screenshot()
img = cv2.imread("VM.png",0) # 0 读入灰度图
img3 = cv2.imread("VM.png",1) # 1 读入彩色图
img2 = img.copy()
#template = cv2.imread("small.png",0)
template = cv2.imread("Maple.png",0)
w, h = template.shape[::-1]


# 6种算法的列表
#methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

methods = ['cv2.TM_CCOEFF']
# 依次使用算法匹配

def initial():
    top_left = (0,0)
    for meth in methods:
        img = img2.copy()
        method = eval(meth)

        # 应用模板算法，返回一系列指标
        res = cv2.matchTemplate(img,template,method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res) # 从res中挑选最优指标
        
        # 注意 TM_SQDIFF 或者 TM_SQDIFF_NORMED 算法使用最小值为最优
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            top_left = min_loc
        else:
            top_left = max_loc

        top_left = [top_left[0] * 1280/2560,top_left[1] * 800/1600]
        print(top_left)
    return top_left

if __name__ == '__main__':
    initial()
