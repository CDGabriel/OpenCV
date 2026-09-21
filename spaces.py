import cv2 as cv
import matplotlib.pyplot as plt
img =cv.imread("Images/witcher.jpg")
def rescale(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
imgRescaled=rescale(img,0.25)

# plt.imshow(imgRescaled)
# plt.show()


# BGR to Grayscale
gray=cv.cvtColor(imgRescaled,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# BGR to HSV
hsv = cv.cvtColor(imgRescaled,cv.COLOR_BGR2HSV)
cv.imshow('Hsv',hsv)

# BGR to L*a*b
lab =cv.cvtColor(imgRescaled,cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)

# BGR to RGB
rgb=cv.cvtColor(imgRescaled,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)

# HSV to BGR
hsv_bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('HsvToBgr',hsv_bgr)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)