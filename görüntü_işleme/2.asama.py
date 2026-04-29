import cv2
import numpy as np
from cvzone.SerialModule import SerialObject

arduino = SerialObject("COM3", 9600)

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
            
            middle_x = frame.shape[1] // 2
            distance_from_middle = center[0] - middle_x
            
            # Dairenin boyutunu hesapla
            pi = 3.14
            area = radius * radius * pi    
            circle_size = np.sqrt(area / pi)  # Dairenin yarıçapını yeniden hesapla
            
            side = ""
            
            # Sağda mı, solda mı, üstte mi, altta mı olduğunu belirle
            if distance_from_middle > circle_size:
                side += "sagda "
                arduino.sendData([2])
            elif distance_from_middle < -circle_size:
                side += "solda "
                arduino.sendData([1])
            else:
                side += "merkezde "

            if center[1] < frame.shape[0] // 2 - circle_size:
                side += "ustte"
                arduino.sendData([3])
            elif center[1] > frame.shape[0] // 2 + circle_size:
                side += "altta"
                arduino.sendData([4])
                
            # Metni görüntüye yazdır
            cv2.putText(frame, side, (center[0], center[1] - 20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 2)
            
            # Nesnenin merkezine ve ortasına yaklaşıldığında "atis" yaz
            if abs(distance_from_middle) <= circle_size and \
                    center[1] >= frame.shape[0] // 2 - circle_size and \
                    center[1] <= frame.shape[0] // 2 + circle_size:
                cv2.putText(frame, "atis", (center[0], center[1] + 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 255), 2)
                
                
        else:
            arduino.sendData([])
    
    # Ortadaki çarpı çizgilerini görüntüye ekle
    cv2.line(frame, (int(frame.shape[1] // 2) - 10, int(frame.shape[0] // 2)), (int(frame.shape[1] // 2) + 10, int(frame.shape[0] // 2)), (255, 255, 255), 2)
    cv2.line(frame, (int(frame.shape[1] // 2), int(frame.shape[0] // 2) - 10), (int(frame.shape[1] // 2), int(frame.shape[0] // 2) + 10), (255, 255, 255), 2)
    
    cv2.imshow('Yuvarlak Tespiti', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('n'):
        break

cap.release()
cv2.destroyAllWindows()


