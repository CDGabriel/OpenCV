import cv2 as cv

img =cv.imread("Images/blckbird.jpg")
def rescale(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
imgRescaled=rescale(img,0.25)

gray = cv.cvtColor(imgRescaled,cv.COLOR_BGR2GRAY)

# Simple Threshloding
threshold, thresh=cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Thershold Simple',thresh)


threshold, thresh_inv=cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Thershold Inverse Simple',thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY, 11, 5)
cv.imshow('Adaptive Thresholding',adaptive_thresh)

cv.waitKey(0)