import cv2

img = cv2.imread('1.jpg', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('1.jpg', cv2.IMREAD_UNCHANGED)
cv2.imshow('gray pic', img)
cv2.waitKey(0)
print('Image Dimensions:', img.shape)
