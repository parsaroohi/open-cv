import cv2

image = cv2.imread('1.jpg')
win_name = 'image'
center = (150, 150)
axes = (100, 50)
angle = 0
startAngle = 0
endAngle = 360
color = (0, 255, 0)
thickness = 1
image = cv2.ellipse(image, center,
                    axes, angle,
                    startAngle, endAngle,
                    color, thickness)
cv2.imshow(win_name, image)
cv2.waitKey(0)
