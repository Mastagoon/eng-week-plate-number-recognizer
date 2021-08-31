import cv2 as cv

img = cv.imread("pp.jpg")

cv.imshow('Image', img)

cv.waitKey(0)