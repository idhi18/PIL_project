from PIL import Image, ImageFilter
img=Image.open("OFF.png")
def ker(img, s, k, sc, off):
    img1=img.filter(ImageFilter.Kernel(s, k, sc, off))
    return img1
# a=ker(img, 20)     #dhundla hua blur
a=ker(img, 20, 15, None, 0)     #dhundla hua blur   
a.show()                                                                   
