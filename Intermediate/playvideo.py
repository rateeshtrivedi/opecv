import cv2

video=cv2.VideoCapture('intro.mp4')

if(video.isOpened()==False):
    print("Error Opening The Video!")

while(video.isOpened()):
    ret, frame=video.read()
    if ret==True:
        cv2.imshow("Frames",frame)

        if cv2.waitKey(0):
            break
    else:
        break

video.release()
cv2.destroyAllWindows()