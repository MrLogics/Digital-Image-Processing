import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('space.tif', 0)
f = np.fft.fft2(img)
f2 = np.fft.fftshift(f)
# f3 = 0.5 * np.log(1+np.abs(f2))
# plt.imshow(f3, cmap="gray")
# plt.show()

m, n = img.shape
p, q = np.meshgrid(np.arange(-np.floor(m/2), np.floor(m/2)), np.arange(-np.floor(n/2), np.floor(n/2)))
D = np.sqrt(p**2 + q**2)
d = 0.38
w = 0.28
C1 = D < (d-(w/2))
C2 = D > (d+(w/2))
C = np.logical_or(C1, C2)
hp = f2 * np.transpose(C)

i = np.fft.ifftshift(hp)
i2 = np.fft.ifft2(i)
i2 = np.abs(i2)
m = np.max(i2)
i2 = i2/m
plt.imshow(i2, cmap="gray")
plt.show()
