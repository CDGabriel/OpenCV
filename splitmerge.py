import cv2 as cv
import numpy as np
img =cv.imread("Images/witcher.jpg")
def rescale(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
imgRescaled=rescale(img,0.25)

blank = np.zeros(imgRescaled.shape[:2],dtype='uint8')

b,g,r=cv.split(imgRescaled)

blue = cv.merge([b,blank,blank])
red = cv.merge([blank,blank,r])
green = cv.merge([blank,g,blank])

cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('Red',r)
cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)

merged = cv.merge([b,g,r])
cv.imshow('Merged',merged)
cv.waitKey(0)