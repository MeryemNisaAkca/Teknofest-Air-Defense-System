import cv2

cap=cv2.VideoCapture('videonun adresi yazılır')

while True:
    ret, frame=cap.read()
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    if ret==False:
        break
    
    if cv2.waitKey(30) & 0xFF==ord('n'):
        break
    
    
cap.release()
cv2.destroyAllWindows()