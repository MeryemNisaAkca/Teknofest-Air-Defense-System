import cv2
import numpy as np
import matplotlib.pyplot as plot


path='02_pixels_operations/forest.jpg'
img=cv2.imread(path)
#print(img)

corner=img[0:500, 0:100]

img[0:100,0:100]=(240,240,1)

cv2.imshow('corner',corner)
cv2.imshow('forest',img)
cv2.waitKey(0)
cv2.destroyAllWindows()