from PIL import ImageTk, Image
def rot(ang, img):
 
    rotated_image = img.rotate(ang)
    return rotated_image