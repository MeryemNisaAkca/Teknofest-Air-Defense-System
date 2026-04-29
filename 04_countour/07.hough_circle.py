import cv2
import numpy as np

img=cv2.imread('04_countour/yuvarlak.jpg')
img1=cv2.imread('04_countour/balls.jpg')
img2=cv2.imread('04_countour/coins.jpg')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

img_blur=cv2.medianBlur(gray,5)
img1_blur=cv2.medianBlur(gray1,5)
img2_blur=cv2.medianBlur(gray2,5)

circles=cv2.HoughCircles(img_blur,cv2.HOUGH_GRADIENT,1,img.shape[0]/4,param1=200,param2=10,minRadius=30,maxRadius=90)
# netleştirilen resim,algılama yöntemi,çözünürlük oranı,min mesafe yuvarlakların arasındaki,methoda özel parametreler

circles=cv2.HoughCircles(img1_blur,cv2.HOUGH_GRADIENT,1,img1.shape[0]/4,param1=200,param2=10,minRadius=35,maxRadius=90)

circles=cv2.HoughCircles(img2_blur,cv2.HOUGH_GRADIENT,1,img2.shape[0]/4,param1=200,param2=10,minRadius=35,maxRadius=90)


if circles is not None:
    circles=np.uint16(np.around(circles))
    
    for i in circles[0,:]:
        cv2.circle(img2,(i[0],i[1]),i[2],(0,255,0),2)
        
cv2.imshow('img',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
        
    








