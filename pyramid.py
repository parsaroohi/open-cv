import cv2
import matplotlib.pyplot as plt

img = cv2.imread('1.jpg')
layer = img.copy()

for i in range(4):
    plt.subplot(2, 2, i+1)
    layer = cv2.pyrDown(layer)
    plt.imshow(layer)
    plt.show()
    cv2.imshow(f'image{i}', layer)
