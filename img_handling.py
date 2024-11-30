import cv2 as cv
import time, os
from PIL import Image

def import_image():
    for i in range(4):
        print(4-i)
        time.sleep(1) #wait for 4 seconds to adjust the camera
        
    cap = cv.VideoCapture(0)
    ret, frame = cap.read()

    cv.imwrite(r'images/unchanged.jpg',frame)
    cv.destroyAllWindows()
    cap.release()