from PIL import Image
Img= Image.open("avarcado.jpg")
def rot(img, angle, resample, expand):
    Img1=img.rotate(angle, resample, expand)
    return Img1
a=rot(Img, 90, 0, 0)
a.show()