
import cv2
import numpy as np

img = cv2.imread('square.tif', 0)

kernel = np.ones((3,3), np.int8)

img2 = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations = 1)

cv2.imshow('Original Image', img)

cv2.imshow('New Image', img2)

cv2.waitKey(0)