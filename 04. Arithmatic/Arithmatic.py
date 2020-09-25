import cv2
import numpy as np

img1 = np.zeros((400,400),np.uint8)
cv2.rectangle(img1,(100,100),(200,300),(255,255,255),-1)
cv2.imshow("Image1",img1)

img2 = np.zeros((400,400),np.uint8)
cv2.rectangle(img2,(100,100),(300,200),(255,255,255),-1)
cv2.imshow("Image2",img2)

img3 = img1+img2
cv2.imshow("Image3",img3)

img4 = img1-img2
cv2.imshow("Image4",img4)

img5 = cv2.bitwise_not(img1)
cv2.imshow("Image5",img5)
