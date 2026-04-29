import cv2
import numpy as np

img=cv2.imread('03_drawing_function/klon.jpg')

kernel=np.ones((5,5),np.uint8)
#şeklin bozulma oraını verir büyüdükçe bozulma artar
#erosion=cv2.erode(img,kernel,iterations=1)
#şekil,bozma oranı, kaçkere bozacağı
#dilation=cv2.dilate(img,kernel,iterations=5)

#cv2.imshow('dilation',dilation)
cv2.imshow('img',img)
#cv2.imshow('erosion',erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()