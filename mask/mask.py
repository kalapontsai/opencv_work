# -*- coding: utf-8 -*-
#製作一個mask,只顯示目標
import cv2
import numpy as np

imgfile = "pcb.jpg"
img = cv2.imread(imgfile)

maskImg = np.zeros(img.shape,np.uint8)

color = (255, 255, 255)
#cv2.line(maskImg, (0, 0), (200, 200), color)
cv2.rectangle(maskImg, (104, 20), (178, 137), color, -1)

# 試試 or , not , xor
image = cv2.bitwise_and(img, maskImg)
#cv2.imwrite("new.jpg", img) #直接畫面而已
cv2.imshow('mask',maskImg)
cv2.imshow('img',img)
cv2.imshow('result',image)
cv2.waitKey(0)