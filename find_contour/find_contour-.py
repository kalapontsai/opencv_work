import cv2
import numpy as np

# 读取图片
img = cv2.imread("shape.jpg")
# 转灰度图片
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  

# 轮廓检测
_ ,contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

newImg = np.zeros(img.shape,np.uint8)  #根据图像的大小来创建一个图像对象
#newImg2 = img.copy() #複製

# 画图
# color : BGR ex: red = 0,0,255 ; blue = 255,0,0
cv2.drawContours(newImg, contours, -10, (0,0,255), 1)  

#儲存
cv2.imwrite("shape-contour.jpg", newImg)

# 展示
cv2.imshow("img", newImg)
cv2.imshow("img2", img)  

# 讀取使用者所按下的鍵
cv2.waitKey(0)



# 關閉圖形顯示視窗
cv2.destroyAllWindows()