import cv2

img=cv2.imread('python.png',cv2.IMREAD_COLOR)

#Shape Property = (Height, Width, Colorspace)

shrink_prec=50
zoom_prec=200

new_width=int(img.shape[1]*shrink_prec/100)
new_height=int(img.shape[0]*shrink_prec/100)

new_width_zoom=int(img.shape[1]*zoom_prec/100)
new_height_zoom=int(img.shape[0]*zoom_prec/100)



dim=(new_width,new_height)
dim_zoon=(new_width_zoom,new_height_zoom)

resize_img=cv2.resize(img,dim,interpolation=cv2.INTER_AREA)
resize_img_zoom=cv2.resize(img,dim_zoon,interpolation=cv2.INTER_AREA)


cv2.imshow("Original Image",img)
cv2.imshow("Resized Image",resize_img)
cv2.imshow("Zoom Image",resize_img_zoom)


cv2.waitKey(0)
#print("Org Width:", img.shape[1])
#print("New Width:", new_width)