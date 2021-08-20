from mss import mss
from PIL import Image
import cv2
mon = {'top':300, 'left':500, 'width':600, 'height':600}
sct = mss()
while True:
	sct.get_pixels(mon)
	frame = Image.frombytes('RGB', (sct.width, sct.height), sct.image)
	frame = np.array(frame)
	cv2.imshow('a crop of the screen', frame)
	if cv2.waitKey(1) & 0xff == ord('q'): 
		cv2.destroyAllWindows()


