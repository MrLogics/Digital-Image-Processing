import cv2
import numpy as np
from matplotlib import pyplot as plt

#IMAGE DIVISION

img=cv2.imread("tissue.tif",0)
shade=cv2.imread("shading.tif",0)
img=np.float64(img)
shade=np.float64(shade)
new_img=img/shade

plt.subplot(131),plt.imshow(img,'gray')
plt.subplot(132),plt.imshow(shade,'gray')
plt.subplot(133),plt.imshow(new_img,'gray')
plt.show()