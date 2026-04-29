import cv2
import numpy as np

canvas=np.zeros((512,512,3),dtype=np.uint8) +255


font1=cv2.FONT_HERSHEY_COMPLEX
font2=cv2.FONT_HERSHEY_DUPLEX
font3=cv2.FONT_ITALIC

cv2.putText(canvas, 'OpenCV', (5,100), font3 , 3, (0,0,0), cv2.LINE_AA)
#çizim yapılacak ekran, metin, yazı başlangıcı sol alt köşe, yazı fontu , font büyüklüğü, renk, tipi  





cv2.imshow('canvas',canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()