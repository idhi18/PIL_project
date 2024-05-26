from PIL import Image, ImageFilter
img=Image.open(r"functions\avarcado.jpg")
def min(img, size):
    minf1=img.filter(ImageFilter.MinFilter(size))
    return minf1
a=min(img, 33)        # blur like apply duster on board
# a=min(img, 3)        
a.show() 