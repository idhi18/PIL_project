from PIL import Image, ImageEnhance
def shr(img, fac):
    s=ImageEnhance.Sharpness(img)
    img1=s.enhance(fac)
    return img1
