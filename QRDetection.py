import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0) # set up camera, number is the device number
cap.set(3, 1920)  # 3 is for width
cap.set(4, 1080)  # 4 is for heigt

while True:
    sucess, img = cap.read()
    for barcode in decode(img):
        myData = barcode.rect
        print(myData)
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, (255, 0, 255), 5)

    cv2.imshow('camera', img)  # Show Camera
    cv2.waitKey(1)  # 1ms delay
