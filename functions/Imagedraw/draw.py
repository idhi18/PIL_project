from PIL import Image, ImageDraw
img=Image.open('OFF.png')
def draw(img, xy, f, out, w):
    dr=ImageDraw.Draw(img)
    img1= dr.rectangle(xy, f, out, w)
    return img
a=draw(img, 
       (30,30,120,120),
       (20,98,60),
       (2,55,25),
       (10))
a.show()

