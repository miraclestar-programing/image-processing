import cv2

img=cv2.imread("Lenna.bmp")
hsv_img=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imwrite("Lenna_HSV.bmp",hsv_img)
