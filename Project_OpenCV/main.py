import cv2
import numpy as np

"""Ctrl+Shift+P
pip3.10 install opencv-python
"""
img = cv2.imread('images/photo1.jpg')
#cv2.imshow('Result', img)

#print(img.shape)

#img = cv2.resize(img, (img.shape[1] * 2, img.shape[0] * 2))
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#img[0:100, 0:150] - обрезка

img = cv2.Canny(img, 200, 200)
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = np.ones((5, 5), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)

img = cv2.erode(img, kernel, iterations=1)

#cv2.imshow('Result', img)

#print(img.shape)

cv2.waitKey(0) 



cap = cv2.VideoCapture('videos/v1.mp4')

cap.set(3, 500)
cap.set(4, 300)

# Вебкамера cap = cv2.VideoCapture(0)
"""while True:
    succes, img = cap.read()
    cv2.imshow('Result', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
"""

""" Распознование лиц
https://github.com/opencv/opencv/tree/4.x/data/haarcascades
"""
img = cv2.imread('images/photo5.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = cv2.CascadeClassifier('face.xml')

results = faces.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=4)

for (x, y, w, h) in results:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=3)

cv2.imshow('Result', img)
cv2.waitKey(0) 