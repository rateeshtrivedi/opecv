import cv2

img=cv2.imread('python.png',cv2.IMREAD_COLOR)

cv2.imshow("Original Image",img)

grayscale_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("GRAY SCALE",grayscale_img)

cv2.waitKey(0)