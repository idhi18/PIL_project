from PIL import Image, ImageFilter
img=Image.open("image\source\OFF.png")
def gaussfil(img, r):
    img1=img.filter(ImageFilter.GaussianBlur(r))
    return img1
#changing value of rad diff intensity 
a=gaussfil(img, 15)   #too much blur smoothing too
# a=gaussfil(img, 5)   # blur
a.show()