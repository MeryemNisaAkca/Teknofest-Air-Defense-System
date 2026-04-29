import cv2
import numpy as np
from collections import deque
from cvzone.SerialModule import SerialObject

arduino = SerialObject("COM3", 9600)


class Nesne:
    def __init__(self, sınıf_numarası, dikdörtgen, merkez, bilgi):
        self.sınıf_numarası = sınıf_numarası
        self.dikdörtgen = dikdörtgen
        self.merkez = merkez
        self.bilgi = bilgi


buffer_size = 16
pts = deque(maxlen=buffer_size)

# Kırmızı renk için HSV aralığı
lower_red1 = np.array([0, 100, 20])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([160, 100, 20])
upper_red2 = np.array([179, 255, 255])

# Kamera seçim kısmı
camera_index = 0  # Varsayılan olarak ilk kamera seçilir
cap = cv2.VideoCapture(camera_index)
cap.set(3, 960)
cap.set(4, 480)

while True:
    success, imgOriginal = cap.read()
    imgOriginal=cv2.flip(imgOriginal, 1)
    if success:
        # Blur
        blurred = cv2.GaussianBlur(imgOriginal, (11, 11), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        # Kırmızı renk için iki maskeyi birleştir
        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
        full_mask = mask1 + mask2

        # Gerekli filtre
        full_mask = cv2.erode(full_mask, None, iterations=2)
        full_mask = cv2.dilate(full_mask, None, iterations=2)

        contours, _ = cv2.findContours(full_mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        nesneler = []
        largest_object = None
        largest_area = 0

        for idx, c in enumerate(contours):
            rect = cv2.minAreaRect(c)
            ((x, y), (width, height), rotation) = rect
            s = "x: {}, y: {}, width: {}, height: {}, rotation: {}".format(np.round(x), np.round(y), np.round(width), np.round(height), np.round(rotation))
            box = cv2.boxPoints(rect)
            box = np.int64(box)

            M = cv2.moments(c)
            if M["m00"] != 0:
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            else:
                center = (0, 0)

            # Nesnenin alanını hesapla
            area = width * height

            # En büyük nesneyi bul
            if area > largest_area:
                largest_area = area
                largest_object = Nesne(idx, rect, center, s)

        if largest_object:
            # En büyük nesneyi işleme al
            rect = largest_object.dikdörtgen
            center = largest_object.merkez
            s = largest_object.bilgi

            box = cv2.boxPoints(rect)
            box = np.int64(box)
            cv2.drawContours(imgOriginal, [box], 0, (0, 255, 255), 2)
            cv2.circle(imgOriginal, center, 5, (255, 0, 255), -1)

            # Referans alan uzunluklarını hesapla
            middle_x = imgOriginal.shape[1] // 2
            distance_from_middle = center[0] - middle_x
            side = ""

            # Sağ sol üst alt tarafında olup olmadığını belirle
            if distance_from_middle > 50:
                side += "sagda "
                arduino.sendData([2])
            elif distance_from_middle < -50:
                side += "solda "
                arduino.sendData([1])
            else:
                side += "merkezde "

            if center[1] < imgOriginal.shape[0] // 2:
                side += "ustte"
                arduino.sendData([3])
            elif center[1] > imgOriginal.shape[0] // 2:
                side += "altta"
                arduino.sendData([4])

            # Nesne ile kameranın ortası arasına çizgi çiz
            cv2.line(imgOriginal, (int(imgOriginal.shape[1] // 2), int(imgOriginal.shape[0] // 2)), center, (255, 255, 255), 2)

            # Nesnenin boyutunu %10 küçült
            object_size = max(rect[1])
            shrinked_size = object_size * 0.10

            cv2.putText(imgOriginal, side, (center[0], center[1] - 20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,
                        (255, 255, 255), 2)

            # Nesnenin merkezine ve ortasına yaklaşıldığında "atis" yaz
            if abs(distance_from_middle) <= shrinked_size and center[1] >= imgOriginal.shape[0] // 2 - shrinked_size and \
                    center[1] <= imgOriginal.shape[0] // 2 + shrinked_size:
                cv2.putText(imgOriginal, "atis", (center[0], center[1] + 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,
                            (255, 255, 255), 2)
        else:
            # Hiçbir nesne tespit edilmediyse Arduino'ya veri gönderme
            arduino.sendData([])

        # Kameranın tam ortasına çarpı çiz
        cv2.line(imgOriginal, (int(imgOriginal.shape[1] // 2) - 10, int(imgOriginal.shape[0] // 2)),
                 (int(imgOriginal.shape[1] // 2) + 10, int(imgOriginal.shape[0] // 2)), (255, 255, 255), 2)
        cv2.line(imgOriginal, (int(imgOriginal.shape[1] // 2), int(imgOriginal.shape[0] // 2) - 10),
                 (int(imgOriginal.shape[1] // 2), int(imgOriginal.shape[0] // 2) + 10), (255, 255, 255), 2)

        cv2.imshow("original tespit", imgOriginal)

    if cv2.waitKey(1) & 0xFF == ord("q"): break

cap.release()
cv2.destroyAllWindows()