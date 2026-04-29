import cv2
import numpy as np

img=cv2.imread('04_countour/contour1.png')
gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

_,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
# min,max, 0 veya 1 yani siyah veya beyaz

contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#print(contours)

cv2.drawContours(img,contours,-1,(0,0,255),3)  #koordinatlar contoursda tutulur,
#0 yazılırsa sadece dış ekran çizilir,
#renkler ve kalınlık

cv2.imshow('new_draw',img)

cv2.waitKey(0)
cv2.destroyAllWindows



