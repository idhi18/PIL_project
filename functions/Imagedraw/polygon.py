from PIL import Image, ImageDraw
img=Image.open('OFF.png')
def draw(img, xy, f, out, w):
    dr=ImageDraw.Draw(img)
    img1= dr.polygon(xy, f, out, w)
    return img1
a=draw(img, 
       [(50,50),(100,0)]
       (255,0,0),
       (0,0,0),
       (3))
a.show()
