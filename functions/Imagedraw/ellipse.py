from PIL import Image, ImageDraw
img=Image.open('OFF.png')
def draw(img, xy, f, out, w):
    dr=ImageDraw.Draw(img)
    img1= dr.ellipse(xy, f, out, w)
    return img
a=draw(img, 
       (30,60,120,120),
       (49,48,90),
       (2,55,25),
       (6))
a.show()
