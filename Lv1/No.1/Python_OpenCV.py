import cv2

img=cv2.imread("Lenna.bmp")
height,width,channel=img.shape
print("しきい値を入力してください(0~255)：")
num=input()
num=int(num)

for a in range(0,height):
    for b in range(0,width):
        if num>int(img[a,b,0]) and num>int(img[a,b,1]) and num>int(img[a,b,2]):
            img[a,b,0]=255
            img[a,b,1]=255
            img[a,b,2]=255
        else:
            img[a,b,0]=0
            img[a,b,1]=0
            img[a,b,2]=0

cv2.imwrite("Lenna_thresholding_opencv.bmp",img)
