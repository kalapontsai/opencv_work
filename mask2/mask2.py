# -*- coding: utf-8 -*-
#依照讀取圖檔大小,切割若干大小,製作mask圖檔
import os
import cv2
import numpy as np

def savejpg(filename,img):
	save_dir = os.getcwd() + '\\example'
	if not os.path.isdir(save_dir): #檢查目錄是否存在
		os.mkdir(save_dir)

	filename = save_dir + '\\' + filename
	while os.path.isfile(filename + '.jpg'): #相同檔名在副檔名加字
			filename += ".1"
	cv2.imwrite(filename + '.jpg',img)

def make_mask(img_name,x1,x2,y1,y2,img):
	maskImg = np.zeros(img.shape,np.uint8)
	cv2.rectangle(maskImg, (x1, y1), (x2, y2), (255,255,255), -1)
	mask_image = cv2.bitwise_and(img, maskImg)
	savejpg(img_name,mask_image)
	#cv2.imshow(img_name,mask_image)

# 取樣方塊的尺寸
block_x = 133
block_y = 133

imgfile = "pcb.jpg"
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
color = (0, 0, 255)

mask_index = '1'

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
		cv2.rectangle(Img, (x_begin, y_begin), (x_end, y_end), color, 1)

		#寫入編號
		txt_x = x_begin + 5
		txt_y = y_begin +10
		cv2.putText(Img, str(block), (txt_x, txt_y), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 0), 1, cv2.LINE_AA)
		
		#產生遮罩圖
		mask_file = str(os.path.splitext(imgfile)[0]) + '-mask' + str(block)
		make_mask(mask_file,x_begin,x_end,y_begin,y_end,img)

savejpg(os.path.splitext(imgfile)[0] + '-mask', Img)
cv2.imshow('show',Img)
cv2.waitKey(0)
cv2.destroyAllWindows()





