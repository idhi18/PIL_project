# importing image object from PIL
import math
from PIL import Image, ImageDraw
w, h = 220, 190
shape = [(40, 40), (w - 10, h - 10)]
# creating new Image object
img = Image.new("RGB", (w, h))
# create rectangle image
img1 = ImageDraw.Draw(img)
img1.arc(shape, start = 20, end = 130, fill ="red")
img.show()

from PIL import Image, ImageDraw
img=Image.open('OFF.png')
def draw(img, xy, s, e, f, w, h):
    dr=ImageDraw.Draw(img)
    img1= dr.arc(xy, s, e, f, w, h)
    return img
a=draw(img, )
a.show()