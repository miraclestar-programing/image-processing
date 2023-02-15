from PIL import Image
import math
import numpy as np

def smoothing_filter(img,ksize_h,ksize_w,sd):
    height=img.height
    width=img.width
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
            sum_r=0
            sum_g=0
            sum_b=0
            for e in range(0,ksize_h*ksize_w):
                sum_r=sum_r+img_r[e]
                sum_g=sum_g+img_g[e]
                sum_b=sum_b+img_b[e]

            ave_r=int(sum_r/(ksize_h*ksize_w))
            ave_g=int(sum_g/(ksize_h*ksize_w))
            ave_b=int(sum_b/(ksize_h*ksize_w))

            new_img2.putpixel((a+th,b+tw),(ave_r,ave_g,ave_b))
            img_r=[]
            img_g=[]
            img_b=[]        
    return new_img2

img=Image.open("Lenna.bmp")
img_i=smoothing_filter(img,3,3,0.5)
img_i.save("Lenna_smoothing_filter.bmp")
