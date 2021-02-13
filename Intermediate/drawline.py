import cv2

img=cv2.imread('python.png',cv2.IMREAD_COLOR)

img=cv2.line(img,(0,0),(250,250),(0,255,0),2)

cv2.imshow("Image",img)

cv2.waitKey(0)