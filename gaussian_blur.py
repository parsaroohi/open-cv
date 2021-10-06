import cv2

img = cv2.imread('1.jpg')
gaussian = cv2.GaussianBlur(img, (7, 7), 0)

cv2.imshow('image', gaussian)
cv2.waitKey(0)
