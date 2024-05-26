from PIL import Image, ImageFilter
def det(img):
    img1=img.filter(ImageFilter.DETAIL)
    return img1
