import cv2
import numpy as numpy

def creSketch(image):
    img_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    img_blur=cv2.GaussianBlur(img_gray,(5,5),0)

    cannyedge=cv2.Canny(img_blur,10,70)

    ret, mask = cv2.threshold(cannyedge,70,2500,cv2.THRESH_BINARY_INV)
    return mask


capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    cv2.imshow('Original', frame)
    cv2.imshow('Sketch',creSketch(frame))

    if cv2.waitKey(1)==13:
        break

capture.release()
cv2.destroyAllWindows()