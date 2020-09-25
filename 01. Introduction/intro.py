import cv2

img = cv2.imread("Sunflower.jpg")

cv2.namedWindow("Image1",cv2.WINDOW_NORMAL)
cv2.imshow("Image1",img)

k = cv2.waitKey(0)
if k == ord('s'):
    cv2.imwrite("new_temp.png",img)
    cv2.destroyAllWindows()
elif k == ord('q'):
    cv2.destroyAllWindows()
