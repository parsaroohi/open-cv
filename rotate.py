import cv2

img = cv2.imread('1.jpg')
# print(type(img))
# print(img.shape)

img1 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
img2 = cv2.flip(img, 0)
cv2.imwrite('image-3.jpg', img1)
cv2.imwrite('image-4.jpg', img2)
