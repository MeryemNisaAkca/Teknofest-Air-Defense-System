import cv2
import numpy as np


canvas=np.zeros((512,512,3),dtype=np.uint8) +255

cv2.line(canvas, (50,50), (510,510), (255,0,0), thickness=5)
#şeklin çizdirileceği yer, şeklin başlangıç noktası, şeklin bitiş noktası, şeklin rengi, şeklin kalınlığı

cv2.rectangle(canvas, (20,20), (150,150), (0,255,0), thickness=-1)
#dikdörtgen oluşturmak için bu fonk kullanılır eger içini doldurmak istersek kalınlık -1 yapılır istemezsek kenar kalınlığı seçeriz

cv2.circle(canvas, (250,250), 100, (0,0,255), thickness=-1)
#merkez noktası ve yarı çap

p1=(100,200)
p2=(50,50)
p3=(300,100)

cv2.line(canvas, p1, p2, (0,0,0), 4)
cv2.line(canvas, p2, p3, (0,0,0), 4)
cv2.line(canvas, p3, p1, (0,0,0), 4)
#üçgen için çizgileri birleştiririz


points=np.array([[[110,200],[330,200],[290,220],[100,100]]],np.int32)
cv2.polylines(canvas, [points], True, (0,0,100), 5)




cv2.imshow('canvas',canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()