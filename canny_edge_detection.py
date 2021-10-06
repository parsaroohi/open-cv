import cv2

img = cv2.imread('1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(gray, (7, 7), 0)
cv2.imshow('original', blurred_image)
canny = cv2.Canny(blurred_image, 10, 30)
cv2.imshow('canny', canny)
cv2.waitKey(0)
