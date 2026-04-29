import cv2
import numpy as np
import matplotlib.pyplot as plt

path='02_pixels_operations/opencv.jpg'
img=cv2.imread(path)

print(img.shape)

print('width:{}'.format(img.shape[0]))
print('height:{}'.format(img.shape[1]))
print('channel:{}'.format(img.shape[2]))

print('image size: {}'.format(img.size))
print(' data type:{}'.format(img.dtype))




cv2.imshow('opencv',img)
cv2.waitKey(0)
cv2.destroyAllWindows()