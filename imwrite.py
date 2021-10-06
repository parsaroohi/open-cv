import cv2
import numpy as np

img = np.random.randint(255, size=(300, 600, 3))
iswritten = cv2.imwrite('image-1.png', img)

if iswritten:
    print('this image saved Successfully')
