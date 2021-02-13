import cv2

image=r'C:\opencvdev\rgb.png'

img=cv2.imread(image,cv2.IMREAD_COLOR)

Blue, Green, Red = cv2.split(img)

cv2.imshow("Original",img)
cv2.imshow("Blue",Blue)
cv2.imshow("Green",Green)
cv2.imshow("Red",Red)

cv2.waitKey(0)

cv2.destroyAllWindows()
