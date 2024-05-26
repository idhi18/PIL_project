from PIL import Image, ImageFilter
Img=Image.open(r"functions\avarcado.jpg")
def mod(img, size):
    img1=img.filter(ImageFilter.ModeFilter(size))
    return img1
a=mod(Img, 5)    #alphabet is looking not clear idhar udhar
a=mod(Img, 50)    #idhar udhar ka sab mix 
a=mod(Img, -50)    #ino effect
a.show()



