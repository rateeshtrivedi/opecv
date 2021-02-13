import cv2

img=cv2.imread('subimage1.png',cv2.IMREAD_COLOR)

cv2.imshow("Original Image",img)

bconst = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT)

cv2.imshow("Border Image",bconst)

cv2.waitKey(0)