from PIL import Image, ImageFilter
img=Image.open("OFF.png")
def med(img, size):
    med1=img.filter(ImageFilter.MedianFilter(size))
    return med1
a=med(img, 33)        # blur with lightning
a=med(img, 3)        # blur with lightning
a.show() 