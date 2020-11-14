import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('cameraman.tif', 0)
f = np.fft.fft2(img)
f2 = np.fft.fftshift(f)
f3 = 0.5 * np.log(1+np.abs(f2))
plt.imshow(f3, cmap="gray")
plt.show()

i = np.fft.ifftshift(f2)
i2 = np.fft.ifft2(i)
i2 = np.abs(i2)
plt.imshow(i2, cmap="gray")
plt.show()
