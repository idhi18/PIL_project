from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from rotate import rot
from contour import cont
from smoot import smoo
from detail import det
from boxblur import boxfilt
from sharp import shr
from bright import br


angle = 0
image_address = ""
IMG = ""

def resize_img(img):
    return img.resize((250, 250), Image.LANCZOS)

def openImage():
    global image_address, IMG
    image_address = filedialog.askopenfilename()
    IMG = Image.open(image_address)
    resizedImage = IMG.resize((250, 250), Image.LANCZOS)
    img = ImageTk.PhotoImage(resizedImage)
    imagePanel.config(image=img)
    imagePanel.image = img
    openImageBtn.config(state=DISABLED)
    removeImageBtn.config(state=NORMAL)
    rotateBtnClock.config(state=NORMAL)
    rotateBtnAnti.config(state=NORMAL)
    contourBtn.config(state=NORMAL)
    smoothBtn.config(state=NORMAL)
    detailBtn.config(state=NORMAL)
    blueScale.config(state=NORMAL)  # Enable the blur scale
    sharpScale.config(state=NORMAL)
    brightScale.config(state=NORMAL)


def removeImage():
    global image_address
    image_address = ""
    IMG = ""
    imagePanel.config(image=None)
    imagePanel.image = None
    openImageBtn.config(state=NORMAL)
    removeImageBtn.config(state=DISABLED)
    rotateBtnClock.config(state=DISABLED)
    rotateBtnAnti.config(state=DISABLED)
    contourBtn.config(state=DISABLED)
    smoothBtn.config(state=DISABLED)
    detailBtn.config(state=DISABLED)
    blueScale.config(state=DISABLED)  # Disable the blur scale
    sharpScale.config(state=DISABLED)
    brightScale.config(state=DISABLED)


# Function to rotate and resize the image
def handleRotate(value):
    global angle, IMG
    rotated_image = rot(value, IMG)
    IMG = rotated_image
    rotated_image = resize_img(rotated_image)
    rotated_img_tk = ImageTk.PhotoImage(rotated_image)
    imagePanel.config(image=rotated_img_tk)
    imagePanel.image = rotated_img_tk

def handleContour():
    global IMG
    contour_image = cont(IMG)
    IMG = contour_image
    contour_image = resize_img(contour_image)
    contour_image_tk = ImageTk.PhotoImage(contour_image)
    imagePanel.config(image=contour_image_tk)
    imagePanel.image = contour_image_tk

def handleSmooth():
    global IMG
    smooth_image = smoo(IMG)
    IMG = smooth_image
    smooth_image = resize_img(smooth_image)
    smooth_image_tk = ImageTk.PhotoImage(smooth_image)
    imagePanel.config(image=smooth_image_tk)
    imagePanel.image = smooth_image_tk

def handleDetails():
    global IMG
    detail_image = det(IMG)
    IMG = detail_image
    detail_image = resize_img(detail_image)
    detail_image_tk = ImageTk.PhotoImage(detail_image)
    imagePanel.config(image=detail_image_tk)
    imagePanel.image = detail_image_tk

def handleBlur():
    global IMG, blurVariable
    blur_image = boxfilt(IMG, blurVariable.get())
    IMG = blur_image
    blur_image = resize_img(blur_image)
    blur_image_tk = ImageTk.PhotoImage(blur_image)
    imagePanel.config(image=blur_image_tk)
    imagePanel.image = blur_image_tk

def handleSharp():
    global IMG, sharpVariable
    sharp_image = shr(IMG, sharpVariable.get())
    IMG = sharp_image
    sharp_image = resize_img(sharp_image)
    sharp_image_tk = ImageTk.PhotoImage(sharp_image)
    imagePanel.config(image = sharp_image_tk)
    imagePanel.image = sharp_image_tk

def handleBrightness():
    global IMG, brightnessVariable
    bright_image = br(IMG, brightnessVariable.get())
    IMG = bright_image
    bright_image = resize_img(bright_image)
    bright_image_tk = ImageTk.PhotoImage(bright_image)
    imagePanel.config(image = bright_image_tk)
    imagePanel.image = bright_image_tk

root = Tk()
root.title("Image Manipulator 1.0")
blurVariable = IntVar()
sharpVariable = IntVar()
brightnessVariable = IntVar()

imageFrame = LabelFrame(root, text="Image", bg="green", padx=50, pady=50)
imageFrame.grid(row=0, column=1, padx=10, pady=10)

imagePanel = Label(imageFrame)
imagePanel.grid(row=1, column=0)

openImageBtn = Button(imageFrame, text="Select Image", command=openImage, anchor=CENTER)
openImageBtn.grid(row=0, column=0)

removeImageBtn = Button(imageFrame, text="Remove Image", command=removeImage, anchor=CENTER)
removeImageBtn.grid(row=2, column=0)

controlFrame = LabelFrame(root, text="Controls", bg="yellow", padx=10, pady=10)
controlFrame.grid(row=0, column=0, padx=10, pady=10)

rotateLabel = Label(controlFrame, text="Rotate Image").grid(row=0, column=0, sticky='w', padx=5, pady=5)
rotateBtnAnti = Button(controlFrame, text="Rotate anti-clockwise", command=lambda: handleRotate(90))
rotateBtnAnti.grid(row=1, column=0, sticky='w')

rotateBtnClock = Button(controlFrame, text="Rotate clockwise", command=lambda: handleRotate(-90))
rotateBtnClock.grid(row=1, column=1, sticky='w')

contourLabel = Label(controlFrame, text="Contour").grid(row=3, column=0, sticky='w', padx=5, pady=5)
contourBtn = Button(controlFrame, text="apply contour", command=handleContour)
contourBtn.grid(row=4, column=0, sticky='w')

smoothLabel = Label(controlFrame, text="Smooth").grid(row=5, column=0, sticky='w', padx=5, pady=5)
smoothBtn = Button(controlFrame, text="apply smooth", command=handleSmooth)
smoothBtn.grid(row=6, column=0, sticky='w')

detailLabel = Label(controlFrame, text="Details").grid(row=7, column=0, sticky='w', padx=5, pady=5)
detailBtn = Button(controlFrame, text="apply details", command=handleDetails)
detailBtn.grid(row=8, column=0, sticky='w')

blurLabel = Label(controlFrame, text="Blur").grid(row=9, column=0, sticky='w', padx=5, pady=5)
blueScale = Scale(controlFrame, orient=HORIZONTAL, from_=0, to=10, length=300, tickinterval=2, label="blur", variable=blurVariable, command=lambda _: handleBlur())
blueScale.grid(row=10, column=0, sticky='w', columnspan=10)
blueScale.config(state=DISABLED)  # Disable the blur scale initially

sharpLabel = Label(controlFrame, text = "Sharp").grid(row=11, column=0, sticky='w',padx=5, pady=5)
sharpScale = Scale(controlFrame, orient=HORIZONTAL, from_=0, to=10, length=300, tickinterval=2, label="sharp", variable=sharpVariable, command=lambda _:handleSharp())
sharpScale.grid(row=12, column=0, sticky='w', columnspan=10)
sharpScale.config(state=DISABLED)

brightLabel = Label(controlFrame, text='Brightness').grid(row=13, column=0, sticky='w', padx=5, pady=5)
brightScale = Scale(controlFrame, orient=HORIZONTAL, from_=0, to=10, length=300, tickinterval=2, label="brightness", variable=brightnessVariable, command=lambda _:handleBrightness())
brightScale.grid(row=14, column=0, sticky='w', columnspan=10)
brightScale.config(state=DISABLED)

if image_address == "":
    rotateBtnClock.config(state=DISABLED)
    rotateBtnAnti.config(state=DISABLED)
    contourBtn.config(state=DISABLED)
    smoothBtn.config(state=DISABLED)
    detailBtn.config(state=DISABLED)
    blueScale.config(state=DISABLED)  # Disable the blur scale
    sharpScale.config(state=DISABLED)
    brightScale.config(state=DISABLED)

root.mainloop()
