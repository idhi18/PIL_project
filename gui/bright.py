from PIL import Image, ImageEnhance
def br(img, fac):
    brg=ImageEnhance.Brightness(img)
    img=brg.enhance(fac)
    return img

