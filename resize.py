import cv2

img = cv2.imread('1.jpg', cv2.IMREAD_UNCHANGED)
new_height = 200
size = (img.shape[1], new_height)
output = cv2.resize(img, size, interpolation=cv2.INTER_AREA)
cv2.imwrite('image-2.jpg', output)
