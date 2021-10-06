import cv2

img = cv2.imread('1.jpg')

B, G, R = cv2.split(img)

cv2.imshow('original', img)
cv2.imshow('blue', B)
cv2.imshow('green', G)
cv2.imshow('red', R)
cv2.waitKey(0)
