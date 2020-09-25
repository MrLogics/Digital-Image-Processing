import cv2
import numpy as np
from matplotlib import pyplot as plt

#IMAGE SUBTRACTION

img=cv2.imread("Angio.tif",0)
shade=cv2.imread("Mask.tif",0)
img=np.float64(img)
shade=np.float64(shade)
new_img=shade-img

plt.subplot(131),plt.imshow(img,'gray')
plt.subplot(132),plt.imshow(shade,'gray')
plt.subplot(133),plt.imshow(new_img,'gray')
plt.show()