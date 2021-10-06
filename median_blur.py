import cv2

img = cv2.imread('1.jpg')
median = cv2.medianBlur(img, 5)

cv2.imshow('image', median)
cv2.waitKey(0)
