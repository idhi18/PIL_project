from PIL import Image, ImageEnhance
img=Image.open("functions\OFF.png")
def shr(img, fac):
    s=ImageEnhance.Sharpness(img)
    img1=s.enhance(fac)
    return img1
