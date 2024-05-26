from PIL import Image,ImageFilter
Img=Image.open("OFF.png")
def mulfil(img):
    img1=img.filter(ImageFilter.MultibandFilter())
    return img1
a=mulfil(Img)
a.show()