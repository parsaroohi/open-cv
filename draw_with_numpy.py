import numpy as np
import cv2

img = np.zeros((400, 400, 3))
cv2.line(img, (20, 160), (100, 200), (0, 0, 255), 12)
cv2.imshow('Numpy', img)
cv2.waitKey(0)
