import cv2  

# 读取图片
img = cv2.imread("find_contour.jpg")
# 转灰度图片
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  

# 轮廓检测
_ ,contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# 新打开一个图片
newImg = cv2.imread("find_contour-add.jpg")
#newImg = cv2.resize(newImg, (300,250))

# 画图
# color : BGR ex: red = 0,0,255 ; blue = 255,0,0
cv2.drawContours(newImg, contours, -10, (0,0,255), 1)  

#儲存
#cv2.imwrite("find_contour-add.jpg", newImg)

# 展示
cv2.imshow("img", newImg)  

# 讀取使用者所按下的鍵
cv2.waitKey(0)



# 關閉圖形顯示視窗
cv2.destroyAllWindows()