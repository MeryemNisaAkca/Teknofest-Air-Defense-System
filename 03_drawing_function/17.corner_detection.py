import cv2
import numpy as np


img=cv2.imread('03_drawing_function/contour.png')
img2=cv2.imread('03_drawing_function/text.png')

gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
gray=np.float32(gray)
# gray işleme sokulmak için floata dönüştürülür

corners=cv2.goodFeaturesToTrack(gray,50,0.01,10)
#renk, bulunması istenen köşe sayısı,kalite,köşeler arası uzaklık

corners=np.int0(corners)
# integera çevirir çember için float kullanılmaz

for corner in corners:
    x,y=corner.ravel()  # değerleri x ve y olarak tek satır haline getirir. x ve y çemberin merkezidir
    cv2.circle(img2,(x,y),3,(0,0,255),-1)
    
cv2.imshow('corner',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
    
