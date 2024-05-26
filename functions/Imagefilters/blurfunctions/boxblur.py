from PIL import Image, ImageFilter
img=Image.open("avarcado.jpg")
def boxfilt(img, r):
    img=img.filter(ImageFilter.BoxBlur(r))
    return img
# a=boxfilt(img, 3)        #blur
a=boxfilt(img, 20)       # too much blur
# a=boxfilt(img, 0)        #original
a.show()
