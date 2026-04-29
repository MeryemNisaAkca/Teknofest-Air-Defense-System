import cv2
import numpy as np

# Kamera veya videoyu başlat
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Görüntüyü BGR'den HSV'ye dönüştür
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Kırmızı renk aralığını belirle (örneğin, bu örnekte kırmızı tonları)
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    
    # Kırmızı balonları belirlemek için maske oluştur
    mask = cv2.inRange(hsv, lower_red, upper_red)
    
    # Kırmızı balonların kontürlerini bul
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Kontürler üzerinde döngü yaparak balonları çiz
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:  # Belirli bir alan eşiğini (1000 piksel kare) belirleyerek küçük gürültüleri filtreleyebiliriz
            cv2.drawContours(frame, [contour], -1, (0, 255, 0), 3)
    
    cv2.imshow('Original', frame)
    cv2.imshow('Mask', mask)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
