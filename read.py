import cv2 as cv

#read images

img = cv.imread('photos/cat-1.jpg')

cv.imshow('Cats', img)

cv.waitKey(0)

#read videos

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

