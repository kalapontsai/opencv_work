# -*- coding: utf-8 -*-
#依照讀取圖檔大小,切割若干大小,並儲存圖檔
#儲存圖檔為切割後尺寸,非原圖尺寸
import os
import cv2
import numpy as np

def savejpg(filename,img):
	filename = save_dir + '\\' + filename
	while os.path.isfile(filename + '.jpg'): #相同檔名在副檔名加字
			filename += ".1"
	cv2.imwrite(filename + '.jpg',img)

def crop(img_name,x1,x2,y1,y2,img):
	w = x2 - x1
	h = y2 - y1
	crop_img = img[y1:y2, x1:x2]
	savejpg(img_name,crop_img)
	cv2.imshow(img_name,crop_img)

# 取樣方塊的尺寸
block_x = 800
block_y = 800

#原圖檔名
imgfile = "p1.jpg"

#檢查目錄是否存在
save_dir = os.getcwd() + '\\example'
if not os.path.isdir(save_dir): 
	os.mkdir(save_dir)


img = cv2.imread(imgfile)
Img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
h, w, _ = img.shape

print ('shape size: %s x %s' % (w,h))

if w % block_x == 0 :
	row = range(1,w // block_x + 1)
else:
	row = range(1,w // block_x + 2)
	row_more = w % block_x
if h % block_y == 0 :
	col = range(1,h // block_y + 1)
else:
	col = range(1,h // block_y + 2)
	col_more = h % block_y

print ('row = %s column: %s' % (row,col))

block = 0
color_red = (0, 0, 255)
color_green = (0, 255, 0)
color_blue = (255, 0, 0)

print ('start','end')
for x in row :
	x_end = x * block_x
	x_begin = x_end - block_x
	if x_end > w:
		x_end = w
		x_begin = (x-1)* block_x
	for y in col :
		y_end = y * block_y
		y_begin = y_end - block_y
		if y_end > h:
			y_end = h
			y_begin = (y-1)* block_y
		block += 1
		print ( block,x_begin,y_begin,x_end,y_end )
		#畫方框
		cv2.rectangle(Img, (x_begin, y_begin), (x_end, y_end), color_red, 3)

		#寫入編號
		txt_x = x_begin + 15
		txt_y = y_begin +30
		cv2.putText(Img, str(block), (txt_x, txt_y), cv2.FONT_HERSHEY_SIMPLEX, 1, color_blue, 1, cv2.LINE_AA)
		
		#產生切割圖
		crop_file = str(os.path.splitext(imgfile)[0]) + '-crop' + str(block)
		crop(crop_file,x_begin,x_end,y_begin,y_end,Img)

savejpg(os.path.splitext(imgfile)[0] + '-crop', Img)
cv2.imshow('show',Img)
cv2.waitKey(0)
cv2.destroyAllWindows()





