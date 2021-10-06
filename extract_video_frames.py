import cv2
import os

cam = cv2.VideoCapture('capture.mp4')
try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print('Error: creating directory of data')

currentFrame = 0
while True:
    ret, frame = cam.read()
    if ret:
        name = './data/fram'+str(currentFrame)+'.jpg'
        print('extracting...'+name)
        cv2.imwrite(name, frame)
        currentFrame += 1
    else:
        break

cam.release()
