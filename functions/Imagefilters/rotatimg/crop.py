from PIL import Image
Img=Image.open("OFF.png")
def crop(img, width, height, left, right, top, bottom):
    Img1=img.crop(width, height, left, right, top, bottom)



   