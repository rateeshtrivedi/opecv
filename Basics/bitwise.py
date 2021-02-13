import cv2

image1=cv2.imread("bitwiseimage1.png",cv2.IMREAD_COLOR)
image2=cv2.imread("bitwiseimage2.png",cv2.IMREAD_COLOR)

bitwiseand=cv2.bitwise_and(image2,image1,mask=None)
bitwiseor=cv2.bitwise_or(image2,image1,mask=None)
bitwisexor=cv2.bitwise_xor(image2,image1,mask=None)
bitwisenot1=cv2.bitwise_not(image1,mask=None)
bitwisenot2=cv2.bitwise_not(image2,mask=None)


cv2.imshow("Image1",image1)
cv2.imshow("Image2",image2)
cv2.imshow("Bitwise And",bitwiseand)
cv2.imshow("Bitwise OR",bitwiseor)
cv2.imshow("Bitwise XOR",bitwisexor)
cv2.imshow("Bitwise NOT Image 1",bitwisenot1)
cv2.imshow("Bitwise NOT Image 2",bitwisenot2)

cv2.waitKey(0)