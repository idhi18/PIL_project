from PIL import Image, ImageFilter
def smoo(img):
    img1=img.filter(ImageFilter.SMOOTH)
    return (img1)


 