import cv2
import numpy as np

img = cv2.imread("cameraman.tif", 0)
ret, thr = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
cv2.imshow("Original", img)
cv2.imshow("Threshold", thr)
