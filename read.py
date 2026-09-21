import cv2 as cv

img = cv.imread('Images/EvilDead.jpg')

capture = cv.VideoCapture("Videos/hatelook.mp4")

cv.imshow('Evil',img)

while True:
    isTrue, frame = capture.read()
   
    cv.imshow('Evil',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

cv.waitKey(0)
capture.release()
cv.destroyAllWindows()