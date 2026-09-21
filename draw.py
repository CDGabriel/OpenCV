import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')
# cv.imshow('Blank',blank)
# #1. Paint certain colour
blank[200:300,300:400]=0,255,0
cv.imshow('Green',blank)


#2. Draw Rectangle
cv.rectangle(blank,(0,0),(250,250),(255,255,255),thickness=2)
cv.imshow('Rectangle',blank)


#3. Draw Circle
cv.circle(blank,(250,250),40,(0,0,255),thickness=-1)
cv.imshow('Circle',blank)


#4. Draw Line
cv.line(blank,(0,0),(250,250), (0,255,255),thickness=5)
cv.imshow('Line',blank)


#5. Write Text
cv.putText(blank,'Hello',(225,255),cv.FONT_HERSHEY_TRIPLEX,1.2,(0,255,255),thickness=2)
cv.imshow('Text',blank)
if cv.waitKey(20) & 0xFF==ord('d'):
        quit
cv.waitKey(0)