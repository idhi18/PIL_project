from PIL import Image
from PIL import ImageFilter
fuckoff="source/OFF.png"
with Image.open(fuckoff) as img:
    img.load()
# img.show()
# converted_img=img.transpose(Image.FLIP_TOP_BOTTOM)
# converted_img=img.transpose(Image.FLIP_LEFT_BOTTOM)
# converted_img=img.transpose(Image.ROTATE_90)
# converted_img=img.transpose(Image.ROTATE_180)
# converted_img=img.transpose(Image.TRANSPOSE)
# converted_img=img.transpose(Image.TRANSVERSE)
# rotated_img=img.rotate(45)
# rotated_img=img.rotate(45, expand=True)
# converted_img.show()
# rotated_img.show()
# gray_img=img.convert("L")
# gray_img.show()
blur_img=img.filter(ImageFilter.BLUR)
blur_img.show()