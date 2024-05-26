from PIL import Image, ImageEnhance
img=Image.open("functions\OFF.png")
def shr(img, fac):
    s=ImageEnhance.Sharpness(img)
    img1=s.enhance(fac)
    return img1
a=shr(img, 10)    #sharp
# a=shr(img, 50)     #too sharp
# a=shr(img, -1)   #blur
# a=shr(img, -12)   #blur and sharp too
# a=shr(img, 1.0)       #original
a.show()