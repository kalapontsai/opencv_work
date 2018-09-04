#php 3.65 / opencv-python 3.4.2.17 / numpy 1.15.1 / matplotlib 2.2.3
# HistCompare rev.3 add a picture to show the defeat area
# p2a-64-1500-750-250-250.jpg  % device-sn-start_x-start_y-width-height.jpg

import os
import cv2
import numpy as np

def Hist(f):
	imgBGR = cv2.imread(f)
	hist = cv2.calcHist([imgBGR],[0],None,[256],[0, 256])
	return hist

def savejpg(filename,img):
	filename = save_dir + '\\' + filename
	while os.path.isfile(filename + '.jpg'): #相同檔名在副檔名加字
			filename += ".1"
	cv2.imwrite(filename + '.jpg',img)

hData = []
stdMatch = 0.99 #所有圖片符合比對的比例
stdComp = 0.97 #compareHist 下限

dir1 = 'D:\\Kadela\\git\\opencv_work\\img_compare3'
device = 'p3a' #機種名稱, 圖檔名前綴

#讀取總圖
imgFile = dir1 + '\\' + device + '\\' + device + '-origin.jpg' 
img = cv2.imread(imgFile)
#Img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
for Path, Folder, FileName in os.walk(dir1+ '\\' + device):
	for i in FileName:
		if Folder == ['sample'] and str.split(os.path.splitext(i)[0],'-')[1] != 'all': #不包含下一階目錄的檔案
			#print (Path,Folder,i)
			h1 = Hist(os.path.join(Path,i))
			h2 = Hist(os.path.join(Path,'sample',i))
			a = cv2.compareHist(h1,h2,cv2.HISTCMP_CORREL)
			hData.append(round(a,5))  #保留小數5位
			if a < stdComp :
				x_begin = int(str.split(os.path.splitext(i)[0],'-')[2])
				y_begin = int(str.split(os.path.splitext(i)[0],'-')[3])
				x_end = x_begin + int(str.split(os.path.splitext(i)[0],'-')[4])
				y_end = y_begin + int(str.split(os.path.splitext(i)[0],'-')[5])
				cv2.rectangle(img, (x_begin, y_begin), (x_end, y_end), (0,0,255), 10)
				#寫入編號
				txt_x = x_begin + 15
				txt_y = y_begin + 50
				cv2.putText(img, str.split(os.path.splitext(i)[0],'-')[1] , (txt_x, txt_y), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,0), 5, cv2.LINE_AA)

saveFile = dir1 + '\\' + device + '\\sample\\' + device + '-defeat.jpg'	
cv2.imwrite(saveFile,img)
#print (hData)
count = 0
fail = 0
if hData != [] :
	for i in hData :
		count += 1
		if i < stdComp :
			fail += 1
	score = (count-fail)/count
	print ('檢查標準:  比對下限= %s%% 判定合格標準= %s%% ' % (stdComp*100,stdMatch*100))
	if score > stdMatch :
		print ('圖片數:%s  不合格數:%s  分數:%s%%  判 定 結 果 = 合格' % (count,fail,score*100))
	else:
		print ('圖片數:%s  不合格數:%s  分數:%s%%  判 定 結 果 = 不及格' % (count,fail,score*100))
else:
	print (' == No data ==')