import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('gamma.tif', 0)
g = 3
img = img/255
new_img = (img ** g)
new_img = new_img * 255
new_img = np.array(new_img, dtype=np.uint8)
cv2.imshow("gamma", new_img)