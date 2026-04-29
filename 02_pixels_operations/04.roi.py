# ROI: region of interest
import cv2
import numpy as np
import matplotlib.pyplot as plt


path='02_pixels_operations/starfish.jpg'
img=cv2.imread(path)
print('shape: {}'.format(img.shape))
roi=img[0:100, 0:100]
img[300:400, 200:300]=roi  

# array boyutu aynı olmalı


cv2.imshow('roi',roi)
cv2.imshow('opencv',img)
cv2.waitKey(0)
cv2.destroyAllWindows()