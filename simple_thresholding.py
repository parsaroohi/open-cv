import cv2

img = cv2.imread('1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh1 = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(gray, 120, 255, cv2.THRESH_TRUNC)
# print(ret)
cv2.imshow('binary', thresh1)
cv2.imshow('inv', thresh2)
cv2.imshow('trunc', thresh3)
cv2.waitKey(0)
