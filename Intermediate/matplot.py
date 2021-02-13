import cv2
from matplotlib import pyplot as plt 

img=cv2.imread('python.png',cv2.IMREAD_COLOR) 



plt.imshow(img)
plt.colorbar()
plt.show()

cv2.waitKey(0)