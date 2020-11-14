import cv2
import numpy as np

img = cv2.imread('house.tif', 0)
cv2.imshow("Original", img)

x = cv2.Sobel(img, -1, 0, 1, ksize=3)
y = cv2.Sobel(img, -1, 1, 1, ksize=3)
cv2.imshow("X", x)
cv2.imshow("Y", y)

x = np.array(x, np.float64)
y = np.array(y, np.float64)
z = np.sqrt(x*x + y*y)
z = np.array(z, np.uint8)
cv2.imshow("Sobel", z)
