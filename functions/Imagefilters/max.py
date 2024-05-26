from PIL import Image, ImageFilter
img=Image.open("OFF.png")
def max(img, size):
    max1=img.filter(ImageFilter.MaxFilter(size))
    return max1
a=max(img, 33)        # blur with lightning
a=max(img, 3)        # blur with lightning
a.show() 