from PIL import Image, ImageFilter
Img=Image.open("OFF.png")
def det(img):
    img1=img.filter(ImageFilter.DETAIL)
    return img1
a=det(Img)
a.show()