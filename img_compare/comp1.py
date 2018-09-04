#php 3.65 / opencv-python 3.4.2.17 / numpy 1.15.1 / matplotlib 2.2.3
import cv2
import numpy as np
import matplotlib.pyplot as plt

f1 = 'p2a.jpg'
f2 = 'p2b.jpg'

img1BGR = cv2.imread(f1)
#img1RGB = cv2.cvtColor(img1BGR, cv2.COLOR_BGR2RGB) 
#img1Gray = cv2.cvtColor(img1BGR, cv2.COLOR_BGR2GRAY) 

img2BGR = cv2.imread(f2)
#img2RGB = cv2.cvtColor(img2BGR, cv2.COLOR_BGR2RGB) 
#img2Gray = cv2.cvtColor(img2BGR, cv2.COLOR_BGR2GRAY)


#cv2.calcHist(影像, 通道, 遮罩, 區間數量, 數值範圍)
hist1 = cv2.calcHist([img1BGR],  # 圖片
                    [0],        # channels
                    None,       # mask
                    [256],      # histSize，通常為 [256]
                    [0, 256])    # ranges，通常為 [0, 256]
hist2 = cv2.calcHist([img2BGR],[0],None,[256],[0, 256])

#cv2.HISTCMP_CORREL
#cv2.HISTCMP_CHISQR
#cv2.HISTCMP_INTERSECT 
#cv2.HISTCMP_BHATTACHARYYA
a = cv2.compareHist(hist1,hist2,cv2.HISTCMP_CORREL)

print ('相似度:',a)
#plt.plot(hist1)
#plt.plot(hist2)
#plt.show()

