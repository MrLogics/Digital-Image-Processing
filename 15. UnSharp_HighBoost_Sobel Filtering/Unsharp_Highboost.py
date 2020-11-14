import cv2

img = cv2.imread("DIP.tif", 0)
blur = cv2.GaussianBlur(img, (7, 7), 5)
mask = cv2.subtract(img, blur)
unsharp = cv2.add(img, mask)
hb = cv2.addWeighted(img, 1, mask, 3, 0)


cv2.imshow("Original", img)
cv2.imshow("Blur", blur)
cv2.imshow("Mask", mask)
cv2.imshow("Unsharp", unsharp)
cv2.imshow("High Boost", hb)
