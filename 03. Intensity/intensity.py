import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("Skull.tif",0)

x1=8
x2=4
x3=2

#img=np.array(img).astype(np.uint8)
step1=np.ceil(255/(x1-1))
step2=np.ceil(255/(x2-1))
step3=np.ceil(255/(x3-1))

new_img1=np.round(img/step1)*step1
new_img2=np.round(img/step2)*step1
new_img3=np.round(img/step3)*step1

#new_img1=new_img1.astype(np.uint8)
#new_img2=new_img1.astype(np.uint8)
#new_img3=new_img1.astype(np.uint8)

#cv2.imshow("image", new_image)

plt.subplot(221)
plt.imshow(img,'gray')
plt.axis("off")
plt.title("256 Levels")

plt.subplot(222)
plt.imshow(new_img1,'gray')
plt.axis("off")
plt.title("8 Levels")

plt.subplot(223)
plt.imshow(new_img2,'gray')
plt.axis("off")
plt.title("4 Levels")

plt.subplot(224)
plt.imshow(new_img3,'gray')
plt.axis("off")
plt.title("2 Levels")

plt.show()
#plt.savefig("intensity_levels.png")
