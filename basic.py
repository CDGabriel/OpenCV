import cv2 as cv

img =cv.imread("Images/EvilDead.jpg")
# cv.imshow('Evil',img)

def rescale(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
imgRescaled=rescale(img,0.25)
# Convertong to grayscale
gray=cv.cvtColor(imgRescaled,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Blur
blur =cv.GaussianBlur(imgRescaled,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#Edge Cascade
canny = cv.Canny(imgRescaled,125,175)
cv.imshow('Canny Edges',canny)

# Dilating image
dilated=cv.dilate(canny, (7,7),iterations=3)
cv.imshow('Dilated',dilated)

# Eroding
eroded=cv.erode(dilated,(7,7),iterations=3)
cv.imshow('Eroded',eroded)

# Resize
resize = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('Resize',resize)

# Cropping
cropped=img[50:200,200:400]
cv.imshow('Cropped',cropped)
cv.waitKey(0)