import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 960)
cap.set(4, 480)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_blur = cv2.medianBlur(gray, 5)
    
    # Hough Dönüşümü ile daireleri bul
    circles = cv2.HoughCircles(gray_blur, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=200, param2=30, minRadius=1, maxRadius=50)
    
    if circles is not None:
        circles = np.uint16(np.around(circles))
        
        for circle in circles[0, :]:
            center = (circle[0], circle[1])  # dairenin merkezi
            radius = circle[2]  # dairenin yarıçapı
            
            # Dairenin içine kırmızı bir nokta çizmek için
            cv2.circle(frame, center, 5, (0, 0, 255), -1)
            
            # Daireyi çiz
            cv2.circle(frame, (center[0], center[1]), radius, (0, 255, 0), 2)
    
    cv2.imshow('Yuvarlak Tespiti', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('n'):
        break

cap.release()
cv2.destroyAllWindows()
