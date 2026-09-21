import cv2 as cv
import numpy as np


img =cv.imread("Images/novitec.jpg")

blank =np.zeros(img.shape,dtype='uint8')

def rescale(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
imgRescaled=rescale(img,0.25)

gray = cv.cvtColor(imgRescaled,cv.COLOR_BGR2GRAY)

blur =cv.GaussianBlur(gray,(3,3),cv.BORDER_CONSTANT)
cv.imshow('blur',blur)

canny = cv.Canny(blur,125,175)
cv.imshow('Canny',canny)

ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('thresh',thresh)

contours,hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(len(contours))

cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('Contour',blank)

cv.waitKey(0)