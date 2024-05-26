from PIL import Image, ImageFilter
Img=Image.open("avarcado.jpg")
def count(img):
    img1=img.filter(ImageFilter.CONTOUR)
    return img1
a=count(Img)      #white with light black color fonts
a.show()      