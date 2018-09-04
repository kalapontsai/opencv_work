#php 3.65 / opencv-python 3.4.2.17 / numpy 1.15.1 / matplotlib 2.2.3
import os
import cv2
import numpy as np

def Hist(f):
	imgBGR = cv2.imread(f)
	hist = cv2.calcHist([imgBGR],[0],None,[256],[0, 256])
	return hist

hData = []
stdMatch = 0.99 #所有圖片符合比對的比例
stdComp = 0.97 #compareHist 下限

dir1 = 'D:\\Kadela\\git\\opencv_work\\img_compare2\\device'

for Path, Folder, FileName in os.walk(dir1):
	for i in FileName:
		if Folder == ['sample'] : #不包含下一階目錄的檔案
			#print (Path,Folder,i)
			h1 = Hist(os.path.join(Path,i))
			h2 = Hist(os.path.join(Path,'sample',i))
			a = cv2.compareHist(h1,h2,cv2.HISTCMP_CORREL)
			hData.append(round(a,5))  #保留小數5位
#print (hData)
count = 0
fail = 0
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
