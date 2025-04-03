import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype = 'uint8')
cv.imshow('Blank', blank)

#cng color
# blank[200:300] = 0,145,135
# cv.imshow('Green', blank)

#draw rectangle
# cv.rectangle(blank, (40,70), (300,200), (0,100,250), thickness=-1)
# cv.imshow('Rectangle', blank)

#draw circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 100, (100,100,0), thickness =-1)
# cv.imshow('Circle', blank)

#draw line
# cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (250,250,0), thickness=40 )
# cv.imshow('line', blank)

#write text
cv.putText(blank, 'Hello world!', (10,50), cv.FONT_HERSHEY_TRIPLEX, 1.0, (250,0,250))
cv.imshow('txt',blank)

cv.waitKey(0)