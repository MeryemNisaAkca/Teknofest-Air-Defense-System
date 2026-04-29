import cv2
import numpy as np

img1=cv2.imread('03_drawing_function/bitwise_1.png')
img2=cv2.imread('03_drawing_function/bitwise_2.png')

bit_and=cv2.bitwise_and(img2,img1)
# beyazlar 1 siyahlar 0 dır ve baglacında 0ve0 0 1ve1 1 0ve1 0 dır
bit_or=cv2.bitwise_or(img1,img2)
# 1or1 1   1or0 1   0or0 0
bit_xor=cv2.bitwise_xor(img1,img2)
#1xor0 1   1xor1 0   0xor0 0
bit_not=cv2.bitwise_not(img2)
#tersini verir
bit_not2=cv2.bitwise_not(img1)
#tersini verir


cv2.imshow('bit_not',bit_not)
cv2.imshow('bit_not2',bit_not2)
cv2.imshow('bit_xor',bit_xor)
cv2.imshow('bit_or',bit_or)
cv2.imshow('bit_and',bit_and)
cv2.imshow('img1',img1)
cv2.imshow('img2',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()