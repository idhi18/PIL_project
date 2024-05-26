from PIL import Image,ImageFilter
Img=Image.open("functions\OFF.png")
def edge(img):
    img1=img.filter(ImageFilter.EDGE_ENHANCE)
    return img1
a=edge(Img)
a.show()