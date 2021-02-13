import cv2

img=cv2.imread('nature.png',cv2.IMREAD_COLOR)

edges=cv2.Canny(img,100,200)

cv2.imshow("Original",img)
cv2.imshow("Edges",edges)

cv2.waitKey(0)