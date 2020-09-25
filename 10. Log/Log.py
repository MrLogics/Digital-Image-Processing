import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("log.tif", 0)
c = 255/np.log(1 + np.max(img))
log_pic = c * (np.log(1 + img))
log_pic = np.array(log_pic, dtype=np.uint8)
cv2.imshow("log", log_pic)
