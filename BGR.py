import cv2
import numpy as np

bgr = np.zeros((500,800,3),dtype=np.uint8)
font = cv2.FONT_HERSHEY_SIMPLEX
#AZUL-------------------------------------------------------------
bgr[:100, :200] = (255,0,0)
bgr[:100, 200:400] = (255)
bgr[:100, 400:600] = (0)
bgr[:100, 600:800] = (0)

cv2.putText(bgr,'Azul (255,0,0) -->',(5,55), font, 0.5,(255,255,255),1,cv2.LINE_AA)
cv2.putText(bgr,'B= 255',(220,55), font, 1,(255,0,0),2,cv2.LINE_AA)
cv2.putText(bgr,'G= 0',(440,55), font, 1,(255,0,0),2,cv2.LINE_AA)
cv2.putText(bgr,'R= 0',(640,55), font, 1,(255,0,0),2,cv2.LINE_AA)

#VERDE------------------------------------------------------------
bgr[100:200, :200] = (0,255,0)
bgr[100:200, 200:400] = (0)
bgr[100:200, 400:600] = (255)
bgr[100:200, 600:800] = (0)

cv2.putText(bgr,'Verde (0,255,0) -->',(5,145), font, 0.5,(255,255,255),1,cv2.LINE_AA)
cv2.putText(bgr,'B= 0',(240,155), font, 1,(0,255,0),2,cv2.LINE_AA)
cv2.putText(bgr,'G= 255',(420,155), font, 1,(0,255,0),2,cv2.LINE_AA)
cv2.putText(bgr,'R= 0',(640,155), font, 1,(0,255,0),2,cv2.LINE_AA)

#ROJO------------------------------------------------------------
bgr[200:300, :200] = (0,0,255)
bgr[200:300, 200:400] = (0)
bgr[200:300, 400:600] = (0)
bgr[200:300, 600:800] = (255)

cv2.putText(bgr,'Rojo (0,0,255) -->',(5,245), font, 0.5,(255,255,255),1,cv2.LINE_AA)
cv2.putText(bgr,'B= 0',(240,255), font, 1,(0,0,255),2,cv2.LINE_AA)
cv2.putText(bgr,'G= 0',(440,255), font, 1,(0,0,255),2,cv2.LINE_AA)
cv2.putText(bgr,'R= 255',(620,255), font, 1,(0,0,255),2,cv2.LINE_AA)

#Naranja
bgr[300:400, :200] = (20,117,240)
bgr[300:400, 200:400] = (20)
bgr[300:400, 400:600] = (117)
bgr[300:400, 600:800] = (240)

cv2.putText(bgr,'Naranja(20,117,240)->',(5,345), font, 0.5,(255,255,255),1,cv2.LINE_AA)
cv2.putText(bgr,'B= 20',(230,355), font, 1,(20,117,240),2,cv2.LINE_AA)
cv2.putText(bgr,'G= 117',(420,355), font, 1,(20,117,240),2,cv2.LINE_AA)
cv2.putText(bgr,'R= 240',(620,355), font, 1,(20,117,240),2,cv2.LINE_AA)

bgr[400:500, :200] = (109,45,215)
bgr[400:500, 200:400] = (109)
bgr[400:500, 400:600] = (45)
bgr[400:500, 600:800] = (215)

cv2.putText(bgr,'Rosa (109,45,215)-->',(5,445), font, 0.5,(255,255,255),1,cv2.LINE_AA)
cv2.putText(bgr,'B= 109',(220,455), font, 1,(109,45,215),2,cv2.LINE_AA)
cv2.putText(bgr,'G= 45',(430,455), font, 1,(109,45,215),2,cv2.LINE_AA)
cv2.putText(bgr,'R= 215',(620,455), font, 1,(109,45,215),2,cv2.LINE_AA)

cv2.imshow('B= Blue, G= Green, R= Red',bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()