import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("space.tif", 0)
f = np.fft.fft2(img)
f2 = np.fft.fftshift(f)
# f3 = 0.5 * np.log(1 + np.abs(f2))
# plt.imshow(f3, cmap = 'gray')
# plt.show()

m, n = img.shape
p, q = np.meshgrid(np.arange(-np.floor(m/2), np.floor(m/2)), np.arange(-np.floor(n/2), np.floor(n/2)))
D = np.sqrt(p**2 + q**2)
x = 5
d = 0.28
w = 0.38
C = 1/(1 + (D*w/(D**2 - d**2))**(2*x))

hp = f2 * np.transpose(C)

i = np.fft.ifftshift(hp)
i2 = np.fft.ifft2(i)
i2 = np.abs(i2)
mx = np.max(i2)
i2 = i2/mx
plt.imshow(i2, cmap = 'gray')
plt.show()

