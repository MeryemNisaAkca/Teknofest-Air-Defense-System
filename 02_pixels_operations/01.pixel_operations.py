import cv2
import numpy as np


path='02_pixels_operations\opencv.jpg'
img=cv2.imread(path)

#px=img[100,55]
#print(px)

#(b,g,r)=img[100,30]
#print('red:{}\n blue:{}\n green:{} ' .format(r,b,g))

before=cv2.imshow('before',img)
print(before)
print('before:',img[100,100])
img[100,100]=[1,1,1]
print('after:',img[100,100])
after=cv2.imshow('after',img)
print(after)

cv2.waitKey(0)

cv2.destroyAllWindows()