from PIL import Image, ImageFilter
Img=Image.open("OFF.png")
def smoo(img):
    img1=img.filter(ImageFilter.SMOOTH)
    return (img1)
a=smoo(Img)
a.show()

 