import cv2
import numpy as np
import matplotlib.pyplot as plt
input_filepath = ['pcb.jpg', 'shape1.jpg']
comp_method = [cv2.CV_COMP_CORREL, cv2.CV_COMP_INTERSECT, \
        cv2.CV_COMP_CHISQR, cv2.CV_COMP_BHATTACHARYYA]
# BGR
img = [cv2.imread(i) for i in input_filepath]
hist = [cv2.calcHist([i], [k], None, [256], [0, 256]) for k in range(3) for i in img]
for i in hist:
    for j in i:
        cv2.normalize(j, j)
hist = [np.mean(i, 0) for i in hist]
for method in comp_method:
    d = cv2.compareHist(hist[0], hist[1], method)
    print(d)
# HSV
imgHSV = [cv2.cvtColor(i, cv2.COLOR_BGR2HSV) for i in img]
hist = [cv2.calcHist([i], [0, 1], None, [50, 50], [0, 180, 0, 256]) \
    for i in imgHSV]
for i in hist_set:
    cv2.normalize(i, i)
for method in comp_method:
    d = cv2.compareHist(hist[0], hist[1], method)
    print(d)