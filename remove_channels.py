import cv2
import numpy as np

img = cv2.imread('1.jpg', cv2.IMREAD_UNCHANGED)
print(img.shape)

img[:, :, 1] = np.zeros([img.shape[0], img.shape[1]])
cv2.imshow('image', img)
cv2.waitKey(0)
