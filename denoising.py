import cv2
from matplotlib import pyplot as plt

img = cv2.imread('1.jpg')
dest = cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 15)
plt.subplot(121)
plt.imshow(img)
plt.subplot(122)
plt.imshow(dest)
plt.show()
