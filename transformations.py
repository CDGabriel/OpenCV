import cv2 as cv
import numpy as np

img =cv.imread("Images/EvilDead.jpg")

def rescale(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
imgRescaled=rescale(img,0.25)

# Translation
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

# -x --> LEFT
# -y --> UP
# x --> RIGHT
# y --> DOWN

translated = translate(imgRescaled,100,-100)
cv.imshow('Translated',translated)

# Rotation
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]
    if rotPoint is None:
        rotPoint=(width//2,height//2)

    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)
    return cv.warpAffine(img,rotMat,dimensions)

rotated=rotate(imgRescaled,90)
cv.imshow('Rotated',rotated)

# Resizing
resized = cv.resize(imgRescaled,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('Resize',resized)

# Flipping
flip = cv.flip(imgRescaled, 1)
cv.imshow('Flip',flip)

# Cropping
cropped=img[200:400,300:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)