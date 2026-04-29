import cv2
import numpy as np

cap=cv2.VideoCapture(0)

def nothing(x):
    pass

cv2.namedWindow('Trackbar')
cv2.resizeWindow('Trackbar', 500, 500)

cv2.createTrackbar('lower_h', 'Trackbar', 0, 180, nothing)
cv2.createTrackbar('lower_s', 'Trackbar', 0, 255, nothing)
cv2.createTrackbar('lower_v', 'Trackbar', 0, 255, nothing)

cv2.createTrackbar('upper_h', 'Trackbar', 0, 180, nothing)
cv2.createTrackbar('upper_s', 'Trackbar', 0, 255, nothing)
cv2.createTrackbar('upper_v', 'Trackbar', 0, 255, nothing)

cv2.setTrackbarPos('upper_h', 'Trackbar', 180)
cv2.setTrackbarPos('upper_s', 'Trackbar', 255)
cv2.setTrackbarPos('upper_v', 'Trackbar', 255)

while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)
    
    frame_hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_h=cv2.getTrackbarPos('lower_h', 'Trackbar')
    lower_s=cv2.getTrackbarPos('lower_s', 'Trackbar')
    lower_v=cv2.getTrackbarPos('lower_v', 'Trackbar')
    
    upper_h=cv2.getTrackbarPos('upper_h', 'Trackbar')
    upper_s=cv2.getTrackbarPos('upper_s', 'Trackbar')
    upper_v=cv2.getTrackbarPos('upper_v', 'Trackbar')
    
    lower_color=np.array([lower_h, lower_s, lower_v])
    upper_color=np.array([upper_h, upper_s, upper_v])
    
    mask=cv2.inRange(frame_hsv, lower_color, upper_color)
    
    cv2.imshow('original', frame)
    cv2.imshow('mask',mask)
    
    if cv2.waitKey(20) & 0xFF==ord('n'):
        break
    


cap.release()
cv2.destroyAllWindows()
        

