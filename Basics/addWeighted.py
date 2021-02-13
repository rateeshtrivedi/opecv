import cv2

image1=cv2.imread("addimage1.png",cv2.IMREAD_COLOR)
image2=cv2.imread("addimage2.png",cv2.IMREAD_COLOR)

weigtSum=cv2.addWeighted(image1,0.7,image2,0.3,1)

cv2.imshow("Added Image",weigtSum)

cv2.waitKey(0)