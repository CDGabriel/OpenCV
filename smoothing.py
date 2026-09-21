import cv2 as cv
import numpy as np
img =cv.imread("Images/blckbird.jpg")
def rescale(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
imgRescaled=rescale(img,0.25)

# Averaging
average = cv.blur(imgRescaled,(7,7))
cv.imshow("Average Blur", average)

# Gaussian Blur
gauss = cv.GaussianBlur(imgRescaled,(7,7),0)
cv.imshow('Gaussian Blur',gauss)

# Median Blur
median = cv.medianBlur(imgRescaled,7)
cv.imshow('Median Blur',median)

# Bilateral
bilateral = cv.bilateralFilter(imgRescaled,10,35,25)
cv.imshow('Bilateral Blur',bilateral)


cv.waitKey(0)