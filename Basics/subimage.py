import cv2

image1=cv2.imread("subimage1.png",cv2.IMREAD_COLOR)
image2=cv2.imread("subimage2.png",cv2.IMREAD_COLOR)

subimage=cv2.subtract(image2,image1)

cv2.imshow("Bigger Circle",image1)
cv2.imshow("Smaller Circle",image2)
cv2.imshow("Subtracted Circle",subimage)

cv2.waitKey(0)