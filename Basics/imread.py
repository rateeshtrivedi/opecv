import cv2

image=cv2.imread("python.png",cv2.IMREAD_COLOR)

cv2.imshow("My Python",image)

cv2.waitKey(1000)

cv2.destroyAllWindows()