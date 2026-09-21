import cv2 as cv
import numpy as np
img =cv.imread("Images/blckbird.jpg")
def rescale(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
imgRescaled=rescale(img,0.25)

blank=np.zeros(imgRescaled.shape[:2],dtype='uint8')

mask=cv.circle(blank,(imgRescaled.shape[1]//2-150,imgRescaled.shape[0]//2+200),100,255,-1)
cv.imshow('Mask',mask)

masked = cv.bitwise_and(imgRescaled,imgRescaled,mask=mask)
cv.imshow('Masked img',masked)
cv.waitKey(0)