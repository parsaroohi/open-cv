import cv2
import numpy as np

img = cv2.imread('1.jpg')
win_name = 'erosion'
kernel = np.ones((5, 5))
img = cv2.erode(img, kernel)
cv2.imshow(win_name, img)
cv2.waitKey(0)
