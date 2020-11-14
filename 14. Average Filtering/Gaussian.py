import cv2
import numpy as np

img = cv2.imread('cameraman.tif', 0)
k = cv2.GaussianBlur(img, (5, 5), 10)
cv2.imshow("Original", img)
cv2.imshow("Gaussian", k)
