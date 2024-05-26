from PIL import Image, ImageEnhance
img=Image.open("C:\projects\image\source\OFF.png")
def br(img, fac):
    brg=ImageEnhance.Brightness(img)
    img=brg.enhance(fac)
    return img
a=br(img, 10)     #bright
a=br(img, 50)     #too bright
a=br(img, -1)   #not seen 
a=br(img, 1.0)       #original
a.show()

