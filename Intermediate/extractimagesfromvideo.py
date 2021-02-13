import cv2
import os

newdir=r'D:\copyimage'

video=cv2.VideoCapture('intro.mp4')

currentFrame=0

while(True):
    ret, frame=video.read()

    if ret:
        os.chdir(newdir)
        name=str(currentFrame)+'.jpg'
        print(name)
        cv2.imwrite(name,frame)
        currentFrame=currentFrame+1
    else:
        break

cv2.release()
cv2.destroyAllWindows()