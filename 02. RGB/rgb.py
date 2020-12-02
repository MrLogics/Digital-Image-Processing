import cv2
img=cv2.imread("Sunflower.jpg")
b,g,r = cv2.split(img)
cv2.namedWindow("red",cv2.WINDOW_NORMAL)
cv2.namedWindow("green",cv2.WINDOW_NORMAL)
cv2.namedWindow("blue",cv2.WINDOW_NORMAL)
cv2.imshow("red",r)
cv2.imshow("green",g)
cv2.imshow("blue",b)

img2 = cv2.merge([r,g,b])
cv2.namedWindow("Image2",cv2.WINDOW_NORMAL)
cv2.imshow("Image2",img2)
k = cv2.waitKey(0)
if k == ord('q'):
	cv2.destroyAllWindows()
