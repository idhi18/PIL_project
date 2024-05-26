from PIL import Image, ImageDraw
img=Image.open('OFF.png')
def draw(img, xy, f, w):
    dr=ImageDraw.Draw(img)
    img1= dr.line(xy, f, w)
    return img
a=draw(img, 
       (30,120,120,30),
       (0,32,0),
       (2))
a.show()