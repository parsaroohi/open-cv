import cv2

image = cv2.imread('1.jpg')
text = 'I Love Python'
font = cv2.FONT_HERSHEY_SIMPLEX
org = (00, 185)
fontscale = 1
color = (0, 0, 255)
thickness = 2
image = cv2.putText(image, text, org, font, fontscale, color, thickness,
                    cv2.LINE_AA, False)
cv2.imshow('image', image)
cv2.waitKey(0)
