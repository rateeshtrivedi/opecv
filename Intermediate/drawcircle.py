import cv2

img=cv2.imread('python.png',cv2.IMREAD_COLOR)

row=img.shape[0]
col=img.shape[1]

img=cv2.circle(img,(row//2,col//2),40,(0,0,255),2)

cv2.imshow("Image",img)

cv2.waitKey(0)