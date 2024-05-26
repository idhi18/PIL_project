from PIL import Image, ImageFilter
Img=Image.open("image\source\OFF.png")
def simpfil(img):
    img1=img.filter(ImageFilter.BLUR)
    return img1
a=simpfil(Img)      #simply blur
a.show()