import cv2
import numpy as np

img = cv2.imread('moon.tiff', 0)
k = cv2.Laplacian(img, -1)
sharp = cv2.subtract(img, k)
cv2.imshow("Original", img)
cv2.imshow("Laplacian", k)
cv2.imshow("Sharp", sharp)
