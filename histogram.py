import cv2
from matplotlib import pyplot as plt

img = cv2.imread('1.jpg', 0)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)

# solution 2:
# plt.hist(img.ravel(), 256, [0, 256])

plt.show()
