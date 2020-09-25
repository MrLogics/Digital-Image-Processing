import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('bitplane.tif', 0)
r, c = img.shape
recon = np.full((r, c), 0, np.uint8)
bit = list(range(0, 8))
for k in bit:
    plane = np.full((r, c), 2**k, np.uint8)
    res = cv2.bitwise_and(plane, img)
    new_img = res*255
    cv2.imwrite("bitplane" + str(k) + " .png", new_img)
    if k in [5, 6, 7]:
        recon = cv2.bitwise_or(recon, res)
    cv2.imwrite("bit_recon.png", recon)
