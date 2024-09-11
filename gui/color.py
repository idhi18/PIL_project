from PIL import Image, ImageEnhance
def color(img, fac):
    col=ImageEnhance.Color(img)
    img=col.enhance(fac)
    return img
# a=color(img, 10)         #red
# a=color(img, 1.0)         #original
# a=color(img, -10)             #blue
# a=color(img, 50)         #red too muc
# a=color(img, 0.0)         #black
# a.show()