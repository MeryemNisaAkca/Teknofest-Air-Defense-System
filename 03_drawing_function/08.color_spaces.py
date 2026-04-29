import cv2


img=cv2.imread('01_kutuphane_ekleme/klon.jpg')


img_gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_bgr=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


cv2.imshow('klon_bgr', img_bgr)
cv2.imshow('klon_hsv', img_hsv)
cv2.imshow('klon_gray', img_gray)
cv2.imshow('klon', img)
cv2.waitKey(0)
cv2.destroyAllWindows()