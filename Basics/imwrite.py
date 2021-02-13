import cv2
import os

image_path=r'C:\opencvdev\python.png'

directory=r'C:\copyimage'

img=cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)

os.chdir(directory)

new_filename='newimage.png'

cv2.imwrite(new_filename,img)

print("Saved Successfully!")