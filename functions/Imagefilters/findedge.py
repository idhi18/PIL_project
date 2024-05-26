from PIL import Image, ImageFilter
img=Image.open("OFF.png")
def edfind(img):
    img=img.convert("L")
    img1=img.filter(ImageFilter.FIND_EDGES)
    return img
a=edfind(img)         
a.show()