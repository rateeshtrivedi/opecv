import cv2

img=cv2.imread("python.png",cv2.IMREAD_COLOR)

row=img.shape[0]
col=img.shape[1]

img=cv2.rectangle(img,(0,0),(row,col),(0,255,0),5)

cv2.imshow("Image",img)

cv2.waitKey(0)