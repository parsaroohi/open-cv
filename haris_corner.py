import cv2
import numpy as np

img = cv2.imread('1.jpg')
operate_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
operate_img = np.float32(operate_img)
dest = cv2.cornerHarris(operate_img, 2, 5, 0.07)
dest = cv2.dilate(dest, None)
img[dest > 0.01*dest.max()] = [0, 0, 255]
cv2.imshow('image', img)
cv2.waitKey(0)
