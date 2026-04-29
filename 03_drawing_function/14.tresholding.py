import cv2
import numpy as np
import matplotlib.pyplot as plt


img=cv2.imread('03_drawing_function/klon.jpg',0)

ret,th1=cv2.threshold(img,150,255,cv2.THRESH_BINARY)
#degerlere göre yogunluklar değişir

th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,2)



cv2.imshow('img_th2',th2)
cv2.imshow('img',img)
cv2.imshow('img_th1',th1)
cv2.waitKey(0)
cv2.destroyAllWindows()