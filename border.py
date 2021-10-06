import cv2

img = cv2.imread('1.jpg')
win_name = 'image'
img = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT)
cv2.imshow(win_name, img)
cv2.waitKey(0)
