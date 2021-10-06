import cv2

img_gray = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)
thresh = 128
img_binary = cv2.threshold(img_gray, thresh, 255, cv2.THRESH_BINARY)[1]
cv2.imwrite('image-5.jpg', img_binary)
