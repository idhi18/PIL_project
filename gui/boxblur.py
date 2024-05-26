from PIL import Image, ImageFilter
def boxfilt(img, r):
    img=img.filter(ImageFilter.BoxBlur(r))
    return img

