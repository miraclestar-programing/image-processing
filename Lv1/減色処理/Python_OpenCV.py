import cv2

img=cv2.imread("Lenna.bmp")
cv2.imshow("image",img)
height,width,channels=img.shape[:3]

for h in range(height):
    for w in range(width):
        for c in range(channels):
            if img[h,w,c]>=0 and img[h,w,c]<64:
                img[h,w,c]=32
            elif img[h,w,c]>=64 and img[h,w,c]<128:
                img[h,w,c]=96
            elif img[h,w,c]>=128 and img[h,w,c]<192:
                img[h,w,c]=160
            else:
                img[h,w,c]=224
cv2.imshow("result",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
