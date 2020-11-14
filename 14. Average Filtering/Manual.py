import cv2
import numpy as np

img = cv2.imread('cameraman.tif', 0)
h = np.ones((5, 5), np.float64)/25
k = cv2.filter2D(img, -1, h)
cv2.imshow("Original", img)
cv2.imshow("Manual Average", k)
