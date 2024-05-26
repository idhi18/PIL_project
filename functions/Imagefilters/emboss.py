from PIL import Image, ImageFilter
img=Image.open("functions\OFF.png")
def boss(img):
    img1=img.filter(ImageFilter.EMBOSS)
    return img1
a=boss(img)         #like clay type
a.show()