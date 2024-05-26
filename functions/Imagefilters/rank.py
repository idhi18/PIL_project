from PIL import Image, ImageFilter
Img=Image.open("OFF.png")
def ran(img, size, rank):
    img1=img.filter(ImageFilter.RankFilter(size, rank))
    return img1
# a=ran(Img, 15, 5)    #looking not clear in black color and red color
# a=ran(Img, 23, 50)    #idhar udhar ka sab mix 
a=ran(Img, -50, -30)    #ino effect
a.show()