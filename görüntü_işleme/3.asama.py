import cv2
import numpy as np
from collections import deque #tespit ettiğimiz nesnenin ortasını bulma


buffer_size = 16
pts = deque(maxlen=buffer_size)             #nesne merkezini depolayacak veriler burada depolanır

lower1 = np.array([0, 100, 20])
upper1 = np.array([10, 255, 255])                   #kırmızı renk aralığı 
lower2 = np.array([160,100,20])
upper2 = np.array([179,255,255])

cap = cv2.VideoCapture(0)                   # webcam açılır
cap.set(3,960)     #width
cap.set(4,480)     #height                         #videonun boyutları belirlenir

while True:
    success , imgOriginal = cap.read()
    if success:
        blurred = cv2.GaussianBlur(imgOriginal, (11,11),0)      # resim yumuşatma için kullanılır: video frameleri alınır,yükseklik ve genişlik belirlenir,sınır türü belirlenir
            #detayı azaltıp noise azaltma
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)      # renk skalası hsv ye döndürüldü
        lower_mask = cv2.inRange(hsv, lower1, upper1)        # kırmızı rengin alt degerleri birleştirilir
        upper_mask = cv2.inRange(hsv, lower2, upper2)        #kırmızı rengin üst değerleri birleştirilir
        full_mask = lower_mask + upper_mask                  # alt ve üst degerler birleştirirlir

        full_mask = cv2.erode(full_mask, None, iterations=2)      # erozyon çizgileri inceltir,min pixel değerleri alınır
        full_mask = cv2.dilate(full_mask, None, iterations=2)      #dilation (genişleme) çizgileri büyültür,max pixel değerleri alınır
            #kalan noiselerden kurtulmak için erode ve dilate kullanılır
        contours, _ = cv2.findContours(full_mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  #aynı renk veya yoğunluğa sahip noktaları birleştirir

        nesneler = []  #nesneler dizisi 
        for idx, c in enumerate(contours):
            rect = cv2.minAreaRect(c)  #çizilecek karenin minimum değerde olmasını sağlar
            ((x,y), (width,height), rotation) = rect  #karenin boyutları saptanır
            s = "x: {}, y: {}, width: {}, height: {}, rotation: {}".format(np.round(x),np.round(y),np.round(width),np.round(height),np.round(rotation))
            box = cv2.boxPoints(rect)     #kenarları belirlenen nesneyi bir kutu içine almayı sağlar
            box = np.int64(box)            #sanırsam uzun bu bir kütüphane ve kodu daha hızlı çalıştırıyor

            M = cv2.moments(c)      #görüntü merkezini saptar
            center = (int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"]))

            cv2.drawContours(imgOriginal, [box],0,(0,255,255),2)   #contour çizdirir
            cv2.circle(imgOriginal, center, 5, (255,0,255),-1)     #merkeze nokta çizer
            
            #nesne = Nesne(idx, rect, center, s) 
            #nesneler.append(nesne)
        
        
        for nesne in nesneler:
            cv2.putText(imgOriginal, "Nesne {}".format(nesne.sinif_numarasi), (int(nesne.dikdortgen[0][0]), int(nesne.dikdortgen[0][1]) + 20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 2)
            cv2.putText(imgOriginal, nesne.bilgi, (int(nesne.dikdortgen[0][0]), int(nesne.dikdortgen[0][1]) + 40), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255,255,255), 2)

        cv2.imshow("original tespit",imgOriginal)

    if cv2.waitKey(1) & 0xFF == ord("q"): break  # noqa: E701

cap.release()
cv2.destroyAllWindows()