from PIL import Image, ImageEnhance
img=Image.open("C:\projects\image\source\OFF.png")
def c(img, fac):
    col=ImageEnhance.Color(img)
    img=col.enhance(fac)
    return img
a=c(img, 10)         #red
a=c(img, 1.0)         #original
a=c(img, -10)             #blue
a=c(img, 50)         #red too muc
a=c(img, 0.0)         #black
a.show()