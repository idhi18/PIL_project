from PIL import Image,ImageColor
Img=Image.open("OFF.png")
def rgb(img,color):
    Img1=ImageColor.getrgb(color)
    return Img1
a=rgb(Img, 'orange')
Img2=Image.new('RGB', (100,100),a)
Img2.show()