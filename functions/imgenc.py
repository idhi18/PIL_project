from PIL import Image
from PIL import ImageEnhance
img=Image.open("image\source\me.jpeg")
def enhance_brg(img, factor):
    bg = ImageEnhance.Brightness(img)
    newImg = bg.enhance(factor)
    return newImg
    # img.show()

a = enhance_brg(img, -2)
a.show()
    
