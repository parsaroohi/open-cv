import cv2
import numpy as np

frame = (500, 500)
out = cv2.VideoWriter('Video.avi',
                      cv2.VideoWriter_fourcc(*'DIVX'), 60, frame)

for i in range(0, 255):
    img = np.ones((500, 500, 3))*i
    out.write(img)

out.release()
