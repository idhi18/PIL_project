from PIL import Image, ImageEnhance
img=Image.open("functions\OFF.png")
def cont(img, fac):
    c=ImageEnhance.Contrast(img)
    img=c.enhance(fac)
    return img
a=cont(img, 10)     #red and yellow
a=cont(img, 50)       #red and yellow too much
a=cont(img, -10)       #blue and white
a=cont(img, 1.0)            #original
a.show()