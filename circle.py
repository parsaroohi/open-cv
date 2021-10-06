import cv2

image = cv2.imread('1.jpg')
window_name = 'circle'
center = (120, 50)
radius = 25
color = (255, 0, 0)
thickness = 5
image = cv2.circle(image, center, radius, color, thickness)
cv2.imshow(window_name, image)
cv2.waitKey(0)
