import cv2

image = cv2.imread('1.jpg')
win_name = 'image'
start_point = (20, 20)
end_point = (120, 120)
color = (0, 0, 255)
thickness = -1
image = cv2.rectangle(image, start_point, end_point,
                      color, thickness)
cv2.imshow(win_name, image)
cv2.waitKey(0)
