import cv2 as cv


img = cv.imread('photos/cat-3.jpg')

cv.imshow('Cat', img)

#grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

#edge cascade
canny = cv.Canny(blur, 125, 125)
cv.imshow('Canny Edges', canny)

#dilating image
dilated = cv.dilate(canny, (3,3), iterations = 2)
cv.imshow('Dilated', dilated)

#eroding
eroded = cv.erode(dilated, (3,3),iterations = 2)
cv.imshow("Eroded", eroded)

#resize
resized = cv.resize(img, (500,500), interpolation = cv.INTER_CUBIC)
cv.imshow("Resized", resized)

#cropping
crop = img[50:100, 50:100]
cv.imshow('Crop', crop)

cv.waitKey(0)
