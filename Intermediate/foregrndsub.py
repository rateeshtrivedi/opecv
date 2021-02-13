import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img=cv2.imread('fight.png',cv2.IMREAD_COLOR)

cv2.imshow("Image",img)
cv2.waitKey(0)

mask=np.zeros(img.shape[:2],np.uint8)

backgroundModel=np.zeros((1,65),np.float64)
foregroundModel=np.zeros((1,65),np.float64)

rectangle=(20,100,150,150)

cv2.grabCut(img,mask,rectangle,backgroundModel,foregroundModel,3,cv2.GC_INIT_WITH_RECT)

mask2=np.where((mask==2)|(mask==0),0,1).astype('uint8')

img=img * mask2[:,:,np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()

#cv2.imshow("Original",img)
#cv2.imshow("Mask",mask)

#print(img)
#print(mask)

#cv2.waitKey(0)