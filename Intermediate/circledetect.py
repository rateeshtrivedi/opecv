import cv2

import numpy as np 

img = cv2.imread('marbles.png',cv2.IMREAD_COLOR)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray_blurred=cv2.blur(gray,(3,3))

detected_circle=cv2.HoughCircles(gray_blurred,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=1,maxRadius=40)

if detected_circle is not None:

    detected_circle=np.uint16(np.around(detected_circle))

    for pt in detected_circle[0,:]:
        a,b,r = pt[0],pt[1],pt[2]
        cv2.circle(img,(a,b),r,(0,255,0),2)
        cv2.circle(img,(a,b),1,(0,0,255),3)
        cv2.imshow("Detected Circle",img)

    cv2.waitKey(0)