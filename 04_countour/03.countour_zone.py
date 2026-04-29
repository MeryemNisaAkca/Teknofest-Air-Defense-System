import cv2

img=cv2.imread('04_countour/resim.png')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

M=cv2.moments(contours[0])#agırlık merkezi
#print(M)

cnt=contours[0]  
area=cv2.contourArea(cnt)  # alan

print(area)
print(M['m00'])

perimeter=cv2.arcLength(cnt,True) #çevre
print(perimeter)












