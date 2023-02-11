from PIL import Image
import math
import numpy as np

def gaussian_filter(img,ksize_h,ksize_w,sd):
    height=img.height
    width=img.width
    gaussian_num=[]
    k=0
    th=math.floor(ksize_h/2)
    tw=math.floor(ksize_w/2)
    for h in range(0-th,ksize_h-th):
        for w in range(0-tw,ksize_w-tw):
            k=1/(2*math.pi*pow(sd,2))*math.exp(-(pow(h,2)+pow(w,2))/(2*pow(sd,2)))
            gaussian_num.append(k)

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
            for c in range(0,ksize_h):
                for d in range(0,ksize_w):
                    if c==0 and d==0:
                        sum_r=int(img_r[c*ksize_w+d]*gaussian_num[c*ksize_w+d])
                        sum_g=int(img_g[c*ksize_w+d]*gaussian_num[c*ksize_w+d])
                        sum_b=int(img_b[c*ksize_w+d]*gaussian_num[c*ksize_w+d])
                    else:
                        sum_r=sum_r+int(img_r[c*ksize_w+d]*gaussian_num[c*ksize_w+d])
                        sum_g=sum_g+int(img_g[c*ksize_w+d]*gaussian_num[c*ksize_w+d])
                        sum_b=sum_b+int(img_b[c*ksize_w+d]*gaussian_num[c*ksize_w+d])
            new_img2.putpixel((a+th,b+tw),(sum_r,sum_g,sum_b))
            img_r=[]
            img_g=[]
            img_b=[]
            sum_r,sum_g,sum_b=0,0,0        
    return new_img2

img=Image.open("Lenna.bmp")
img_i=gaussian_filter(img,3,3,0.5)
img_i.save("Lenna_gaussian_filter.bmp")
