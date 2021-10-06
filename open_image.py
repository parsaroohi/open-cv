import cv2

image = cv2.imread('1.jpg')
cv2.imshow('my dog', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
