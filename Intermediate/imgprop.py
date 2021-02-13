import cv2

img=cv2.imread('python.png',cv2.IMREAD_COLOR)


print("Shape: ", img.shape)
print("Size:", img.size)
print('Data Type:', img.dtype)