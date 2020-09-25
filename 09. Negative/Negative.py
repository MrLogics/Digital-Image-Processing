import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("scan.tif", 0)
s = 255 - img
cv2.imshow("Negative", s)



