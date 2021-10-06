import cv2

path = '1.jpg'
image = cv2.imread(path)
window_image = 'Image'
start_point = (0, 0)
end_point = (250, 250)
color = (0, 255, 0)
thickness = 9
image = cv2.line(image, start_point, end_point, color, thickness)
cv2.imshow(window_image, image)
cv2.waitKey(0)
