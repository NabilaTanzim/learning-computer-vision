import cv2 as cv

img = cv.imread('photos/cat-2.jpg')
cv.imshow('Cat', img)

cv.waitKey(0)