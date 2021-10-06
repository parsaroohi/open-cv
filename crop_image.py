import cv2

img = cv2.imread('1.jpg')
y = 0
x = 0
h = 300
w = 500

crop_image = img[x:w, y:h]
cv2.imshow('crop', crop_image)
cv2.imshow('image', img)
cv2.waitKey(0)
