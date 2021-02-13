import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'C:\Users\Administrator\AppData\Local\Programs\Tesseract-OCR\Tesseract.exe'

img=cv2.imread('car.jpeg',cv2.IMREAD_COLOR)

text=pytesseract.image_to_string(img, config='--psm 11')

cv2.imshow("IMage",img)
print("Extracted Text: ",text)

cv2.waitKey(0)