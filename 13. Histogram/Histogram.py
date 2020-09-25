import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('pollen.tif', 0)
plt.hist(img.flatten(), 256, [0, 256], color='r')
equ = cv2.equalizeHist(img)
plt.hist(equ.flatten(), 256, [0, 256], color='b')
plt.show()
cv2.imshow("Equalize", equ)