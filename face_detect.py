import cv2 as cv

img = cv.imread('Images/woman.jpg')

def rescale(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
imgRescaled=rescale(img,0.25)

gray = cv.cvtColor(imgRescaled,cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect= haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=6)

print(len(faces_rect))

for (x,y,w,h) in faces_rect:
    cv.rectangle(imgRescaled,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Detected Faces',imgRescaled)
cv.waitKey(0)