from PIL import Image
import math
import numpy as np

def median_filter(img,ksize_h,ksize_w,sd):
    height=img.height
    width=img.width
    gaussian_num=[]
    k=0
    th=math.floor(ksize_h/2)
    tw=math.floor(ksize_w/2)

    new_height=height+th*2
    new_width=width+tw*2

    new_img=Image.new("RGB",(new_width,new_height),color=0)
    new_img.paste(img,(tw,th))

    new_img2=Image.new("RGB",(new_width,new_height),color=0)
    new_img2.paste(img,(tw,th))

    img_r=[]
    img_g=[]
    img_b=[]

    for a in range(0,new_height-ksize_h):
        for b in range(0,new_width-ksize_w):
            for c in range(0,ksize_h):
                for d in range(0,ksize_w):
                    img_gaso=new_img.getpixel((a+c,b+d))
                    img_r.append(img_gaso[0])
                    img_g.append(img_gaso[1])
                    img_b.append(img_gaso[2])
            for c in range(0,ksize_h*ksize_w-1):
                if img_r[c]>img_r[c+1]:
                    num_r=img_r[c+1]
                    img_r[c+1]=img_r[c]
                    img_r[c]=num_r
            for c in range(0,ksize_h*ksize_w-1):
                if img_g[c]>img_g[c+1]:
                    num_g=img_g[c+1]
                    img_g[c+1]=img_g[c]
                    img_g[c]=num_g
            for c in range(0,ksize_h*ksize_w-1):
                if img_b[c]>img_b[c+1]:
                    num_b=img_b[c+1]
                    img_b[c+1]=img_b[c]
                    img_b[c]=num_b
            median_r=img_r[th*tw]
            median_g=img_g[th*tw]
            median_b=img_b[th*tw]
            new_img2.putpixel((a+th,b+tw),(median_r,median_g,median_b))
            img_r=[]
            img_g=[]
            img_b=[]        
    return new_img2

img=Image.open("Lenna.bmp")
img_i=median_filter(img,3,3,0.5)
img_i.save("Lenna_median_filter.bmp")
