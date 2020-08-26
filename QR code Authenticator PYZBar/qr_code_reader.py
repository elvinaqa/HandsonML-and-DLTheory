import cv2
import numpy as np
from pyzbar.pyzbar import decode

img = cv2.imread('1.png')

code = decode(img)
# print(code)

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    succes, img = cap.read()
    for barcode in decode(img):
        # print(barcode.data)
        # print(barcode.rect)
        my_data = barcode.data.decode('utf-8')
        print(my_data)
        points = np.array([barcode.polygon], np.int32)
        points = points.reshape((-1,1, 2))
        cv2.polylines(img, [points], True, (255, 0, 255), 5)
        pts2 = barcode.rect
        cv2.putText(img, my_data, (pts[0], pts[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
    cv2.imshow('res', img)
    cv2.waitKey(1)
cv2.destroyAllWindows()
