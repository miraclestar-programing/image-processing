from PIL import Image

def ave_pooling(img,ksize_h,ksize_w):
    height=img.height
    width=img.width

    for a in range(0,height,ksize_h):
        for b in range(0,width,ksize_w):
            for c in range(0,ksize_h):
                for d in range(0,ksize_w):
                    if c==0 and d==0:
                        img_gaso=img.getpixel((a+c,b+d))
                        img_r=img_gaso[0]
                        img_g=img_gaso[1]
                        img_b=img_gaso[2]
                        sum_r=img_r
                        sum_g=img_g
                        sum_b=img_b
                    else:
                        img_gaso=img.getpixel((a+c,b+d))
                        img_r=img_gaso[0]
                        img_g=img_gaso[1]
                        img_b=img_gaso[2]
                        sum_r=sum_r+img_r
                        sum_g=sum_g+img_g
                        sum_b=sum_b+img_b
            avg_R=int(sum_r/(ksize_h*ksize_w))
            avg_G=int(sum_g/(ksize_h*ksize_w))
            avg_B=int(sum_b/(ksize_h*ksize_w))
            for c in range(0,ksize_h):
                for d in range(0,ksize_w):      
                    img.putpixel((a+c,b+d),(avg_R,avg_G,avg_B))
    return img

img=Image.open("Lenna.bmp")
img_i=ave_pooling(img,2,2)
img_i.save("Lenna_avpool.bmp")
