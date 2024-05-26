from PIL import Image, ImageFilter
img=Image.open("functions\OFF.png")
def edf(img):
    img=img.convert("L")
    img1=img.filter(ImageFilter.Kernel((3,3),(-1,-1,-1,-1,8,-1,-1,-1,-1),1,0))
    return img1
a=edf(img)         
a.show()   

