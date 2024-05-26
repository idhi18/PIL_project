from PIL import Image, ImageFilter
def cont(img):
    img1=img.filter(ImageFilter.CONTOUR)
    return img1
    