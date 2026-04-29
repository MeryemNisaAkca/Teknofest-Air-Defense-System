import cv2
import numpy as np
import matplotlib.pyplot as plt



path='02_pixels_operations/opencv.jpg'
img=cv2.imread(path)
print('shape: {}'.format(img.shape))

(B,G,R)=cv2.split(img) # renklerine göre resmi split etti

merged=cv2.merge([B,G,R]) # tüm renkleri merged etti


black=np.zeros(img.shape[:2],dtype='uint8')

cv2.imshow('red',cv2.merge([black,black,R]))
cv2.imshow('green',cv2.merge([black,G,black]))
cv2.imshow('blue',cv2.merge([B,black,black]))
cv2.imshow('opencv',img)
#cv2.imshow('opencv-merged',merged)
#cv2.imshow('opencv-B',B)
#cv2.imshow('opencv-G',G)
#cv2.imshow('opencv-R',R)




cv2.waitKey(0)
cv2.destroyAllWindows()