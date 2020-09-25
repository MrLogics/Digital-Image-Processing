import cv2
import numpy as np
from matplotlib import pyplot as plt

#IMAGE AVERAGES

img=cv2.imread("Galaxy.tif",0)
img=np.float64(img)
sum_img=np.zeros((img.shape),np.float64)
mean=0
sigma=20
for i in range(100):
	noise = np.random.normal(mean,sigma,(img.shape))
	noise = img+noise
	sum_img = sum_img + noise

avg = sum_img/i

plt.subplot(131),plt.imshow(img,'gray')
plt.subplot(132),plt.imshow(noise,'gray')
plt.subplot(133),plt.imshow(avg,'gray')
plt.show()
