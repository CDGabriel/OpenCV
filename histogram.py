import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img =cv.imread("Images/novitec.jpg")
def rescale(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
imgRescaled=rescale(img,0.25)
gray = cv.cvtColor(imgRescaled,cv.COLOR_BGR2GRAY)

# Grayscale histogram
gray_hist=cv.calcHist([gray], [0],None,[256],[0,256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('Number of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

#Color Histogram
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('Number of pixels')
colors=('b','g','r')
for i, col in enumerate(colors):
    hist=cv.calcHist([imgRescaled],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()
cv.waitKey(0)