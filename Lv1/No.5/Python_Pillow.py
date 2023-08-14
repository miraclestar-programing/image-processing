from PIL import Image

def max_pooling(img,ksize_h,ksize_w):
    height=img.height
    width=img.width

    for a in range(0,height,ksize_h):
        for b in range(0,width,ksize_w):
            max=[]
            gaso=[]
            for c in range(0,ksize_h):
                for d in range(0,ksize_w):
                    if c==0 and d==0:
                        max=img.getpixel((a+c,b+d))
                        max_r=max[0]
                        max_g=max[1]
                        max_b=max[2]
                    else:
                        gaso=img.getpixel((a+c,b+d))
                        gaso_r=gaso[0]
                        gaso_g=gaso[1]
                        gaso_b=gaso[2]
                        if gaso_r>max_r:
                            max_r=gaso_r
                        if gaso_g>max_g:
                            max_g=gaso_g
                        if gaso_b>max_b:
                            max_b=gaso_b

            for c in range(0,ksize_h):
                for d in range(0,ksize_w):      
                    img.putpixel((a+c,b+d),(max_r,max_g,max_b))
    return img

img=Image.open("Lenna.bmp")
img_i=max_pooling(img,2,2)
img_i.save("Lenna_maxpool.bmp")
