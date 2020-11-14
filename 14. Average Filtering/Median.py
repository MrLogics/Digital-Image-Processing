import cv2
import numpy as np

img = cv2.imread('cameraman.tif', 0)
k = cv2.medianBlur(img, 3)
cv2.imshow("Original", img)
cv2.imshow("Median", k)
