from PIL import Image
import math
import numpy as np

def motion_filter(img,ksize_h,ksize_w):
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
    filter=[]
    for a in range(0,ksize_h):
        for b in range(0,ksize_w):
            k=1/(ksize_w)
            if a==b:
                filter.append(k)
            else:
                filter.append(0)

    for a in range(0,new_height-ksize_h):
        for b in range(0,new_width-ksize_w):
            for c in range(0,ksize_h):
                for d in range(0,ksize_w):
                    img_gaso=new_img.getpixel((a+c,b+d))
                    img_r.append(img_gaso[0])
                    img_g.append(img_gaso[1])
                    img_b.append(img_gaso[2])
            for c in range(0,ksize_h):
                for d in range(0,ksize_w):
                    if c==0 and d==0:
                        img_r2=int(filter[c*ksize_w+d]*img_r[c*ksize_w+d])
                        img_g2=int(filter[c*ksize_w+d]*img_g[c*ksize_w+d])
                        img_b2=int(filter[c*ksize_w+d]*img_b[c*ksize_w+d])
                    else:
                        img_r2=img_r2+int(filter[c*ksize_w+d]*img_r[c*ksize_w+d])
                        img_g2=img_g2+int(filter[c*ksize_w+d]*img_g[c*ksize_w+d])
                        img_b2=img_b2+int(filter[c*ksize_w+d]*img_b[c*ksize_w+d])

            new_img2.putpixel((a+th,b+tw),(img_r2,img_g2,img_b2))
            img_r=[]
            img_g=[]
            img_b=[]
            img_r2=0
            img_g2=0
            img_b2=0        
    return new_img2

img=Image.open("Lenna.bmp")
img_i=motion_filter(img,3,3)
img_i.save("Lenna_motion_filter.bmp")
