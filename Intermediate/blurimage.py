import cv2

img=cv2.imread("capture.png",cv2.IMREAD_COLOR)

cv2.imshow("Original Image",img)

gaussian=cv2.GaussianBlur(img,(7,7),0)

cv2.imshow("Blurred Image",gaussian)

cv2.waitKey(0)