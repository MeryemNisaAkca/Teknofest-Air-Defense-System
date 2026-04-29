import cv2
import numpy as np

img=cv2.imread('03_drawing_function/klon.jpg',0)

row,col=img.shape

M=np.float32([[1,0,10],[0,1,100]]) 
#ilk matris x ekseninde şekli kaydırıyor ikinci matris y ekseninde kaydırıyor

dst=cv2.warpAffine(img,M,(row,col))

cv2.imshow('dst',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()