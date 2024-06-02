import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
from rotate import rot
from sharp import shr
from smoot import smoo
from detail import det
from contour import cont
from bright import br
from boxblur import boxfilt

tk_image = ''
pil_image = ''
image_original = ''
label_aspect_ratio = 0
sharpness_factor = 1.0
brightness_factor = 1.0
boxblurradius_factor = 0

undo_stack = []
redo_stack = []


def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.gif")])
    if file_path:
        display_image(file_path)
        redo_stack.clear()

def remove_image():
    global pil_image 
    push_undo(pil_image)
    pil_image = ''
    image_label.config(image = pil_image)
    image_label.image = pil_image
    messagebox.showinfo("Image Removed", "Image has been removed")
    redo_stack.clear()

def save_image():
    global pil_image
    if pil_image:
        file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*")])
        if file_path:
            pil_image.save(file_path)
            messagebox.showinfo("Image Saved", f"Image saved successfully at {file_path}")
    else:
        messagebox.showwarning("No Image", "No image to save.")

def display_image(file_path):
    global image_original, pil_image
    image_original = Image.open(file_path)
    pil_image = image_original.copy()

    update_display_image()
    undo_stack.clear()
    redo_stack.clear()

def resize_image():
    global pil_image
    if pil_image:
        width, height = pil_image.size
        aspect_ratio = width / height
        if aspect_ratio > label_aspect_ratio:
            new_width = image_label_width
            new_height = int(image_label_width / aspect_ratio)
        else:
            new_height = image_label_height
            new_width = int(image_label_height * aspect_ratio)
        
        return pil_image.resize((new_width, new_height))
    else:
        show_error("Image not found")
           

def update_display_image():
    global pil_image, tk_image, label_aspect_ratio
    pil_image_resized = resize_image()
    tk_image = ImageTk.PhotoImage(pil_image_resized)
    image_label.config(image=tk_image)
    image_label.image = tk_image

def show_error(message):
    messagebox.showerror("Error", message)

def show_feature():
    factor_features_label = ['Sharpness', 'Brightness', 'Blur']
    factor_dec_btn_txt = ['- (min 0.0)', '- (min 0.0)', '- (min 0.0)']
    factor_inc_btn_txt = ['+ (max 2.0)', ' + ', ' + ']
    factor_value_label = {}

    def handle_rotate(value):
        global pil_image
        if pil_image:
            push_undo(pil_image)
            pil_image = rot(value, pil_image)
            pil_image = resize_image()
            update_display_image()
            redo_stack.clear()  
        else:
            show_error("Image not found")
        
    def dec_feature_factor(btn_txt):
        global sharpness_factor, brightness_factor, boxblurradius_factor
        if btn_txt == 'Sharpness':
            if sharpness_factor <= 0:
                messagebox.showerror("Sharpness factor error", "Sharpness factor has reached the minimum limit.")
            else:
                sharpness_factor = round(sharpness_factor - 0.1, 1)  
                factor_value_label[btn_txt].config(text=sharpness_factor)
                messagebox.showinfo("aos","aodimasod+")
        elif btn_txt == 'Brightness':
            if brightness_factor <=0:
                messagebox.showerror("Brightness factor error", "Brightness factor has reached the minimum limit.")
            else:
                brightness_factor = round(brightness_factor - 0.1, 1) 
                factor_value_label[btn_txt].config(text=brightness_factor)
        elif btn_txt == 'Blur':
            if boxblurradius_factor <=0:
                messagebox.showerror("Blur factor error", "Blur factor has reached the minimum limit.")
            else:
                boxblurradius_factor = round(boxblurradius_factor - 0.1, 1)
                factor_value_label[btn_txt].config(text = boxblurradius_factor)
                

    def inc_feature_factor(txt):
        global sharpness_factor, brightness_factor, boxblurradius_factor
        if txt == 'Sharpness':
            if sharpness_factor >=2:
                messagebox.showerror("Sharpness factor error", "Sharpness factor has reached the maximum limit.")
            else:
                sharpness_factor = round(sharpness_factor + 0.1, 1)
                factor_value_label[txt].config(text = sharpness_factor)
        elif txt == 'Brightness':
            brightness_factor = round(brightness_factor + 0.1, 1)
            factor_value_label[txt].config(text = brightness_factor)
        elif txt == 'Blur':
            boxblurradius_factor = round(boxblurradius_factor + 0.1, 1)
            factor_value_label[txt].config(text = boxblurradius_factor)


    def apply(txt):
        global sharpness_factor, pil_image, brightness_factor, boxblurradius_factor
        if pil_image:
            push_undo(pil_image)
            if txt == 'Sharpness':
                pil_image = shr(pil_image, sharpness_factor)
            elif txt == 'Brightness':
                pil_image = br(pil_image, brightness_factor)
            elif txt == 'smooth':
                pil_image = smoo(pil_image)
            elif txt == 'detail':
                pil_image = det(pil_image)
            elif txt == 'contour':
                pil_image = cont(pil_image)
            elif txt == 'Blur':
                pil_image = boxfilt(pil_image, boxblurradius_factor)

            update_display_image()
            redo_stack.clear()
        else:
            show_error("image not found")
    
    def show_factor_value(txt):
        global sharpness_factor, brightness_factor, boxblurradius_factor
        if txt == "Sharpness":
            return sharpness_factor
        elif txt == "Brightness":
            return brightness_factor
        elif txt == "Blur":
            return boxblurradius_factor

    for widgets in feature_frame.winfo_children():
        widgets.destroy()

    # Rotate UI
    tk.Label(feature_frame, text="Rotate").grid(row=0, column=0, pady=5, sticky='w', padx=5, ipady=2, ipadx=2)
    rotate_left = tk.Button(feature_frame, text="Rotate Left", command=lambda: handle_rotate(90))
    rotate_left.grid(row=1, column=0, sticky='w', padx=5, ipady=2, ipadx=2)
    rotate_right = tk.Button(feature_frame, text="Rotate Right", command=lambda: handle_rotate(-90))
    rotate_right.grid(row=1, column=1, sticky='w', padx=5, ipady=2, ipadx=2)

    #smooth ui
    tk.Label(feature_frame, text="Smooth").grid(row=2, column=0, sticky='w', padx=5, ipady=2, ipadx=2, pady=10)
    tk.Button(feature_frame, text="Apply" ,command=lambda: apply('smooth')).grid(row=2, column=1, sticky='ew', padx=5, ipady=2, ipadx=2)

    #detail ui
    tk.Label(feature_frame, text="Detail").grid(row=3, column=0, sticky='w', padx=5, ipady=2, ipadx=2, pady=10)
    tk.Button(feature_frame, text="Apply" ,command=lambda: apply('detail')).grid(row=3, column=1, sticky='ew', padx=5, ipady=2, ipadx=2)

    # contour ui
    tk.Label(feature_frame, text="Contour").grid(row=4, column=0, sticky='w', padx=5, ipady=2, ipadx=2, pady=10)
    tk.Button(feature_frame, text="Apply" ,command=lambda: apply('contour')).grid(row=4, column=1, sticky='ew', padx=5, ipady=2, ipadx=2)

    # Sharpness UI
    
    row_number = 5                       
    for i in range(0, len(factor_features_label)):
        tk.Label(feature_frame, text=factor_features_label[i]).grid(row=row_number, column=0, sticky='w', padx=5, ipadx=2, pady=10, ipady=2)
        row_number += 1

        tk.Button(feature_frame, text=factor_dec_btn_txt[i], command=lambda btn_txt=factor_features_label[i]: dec_feature_factor(btn_txt)).grid(row=row_number, column=0, sticky='ew', padx=5, ipadx=2, ipady=2)

        factor_value_label[factor_features_label[i]] = tk.Label(feature_frame, text=show_factor_value(factor_features_label[i]))
        factor_value_label[factor_features_label[i]].grid(row=row_number, column=1, sticky='nswe', padx=5, ipadx=2, ipady=2)

        tk.Button(feature_frame, text=factor_inc_btn_txt[i], command=lambda txt=factor_features_label[i]: inc_feature_factor(txt)).grid(row=row_number, column=2, sticky='ew', padx=5, ipadx=2, ipady=2) 
        tk.Button(feature_frame, text="Apply", command=lambda txt=factor_features_label[i]: apply(txt)).grid(row=row_number, column=3, sticky='ew', padx=5, ipadx=2, ipady=2)

        row_number += 1






def push_undo(image):
    if image:
        undo_stack.append(image.copy())

def push_redo(image):
    if image:
        redo_stack.append(image.copy())

def undo():
    global pil_image
    if undo_stack:
        push_redo(pil_image)
        pil_image = undo_stack.pop()
        update_display_image()

def redo():
    global pil_image
    if redo_stack:
        push_undo(pil_image)
        pil_image = redo_stack.pop()
        update_display_image()

base = tk.Tk()
base.title('Image Manipulator 1.0')
base.geometry("1200x600")
base.config(bg="#f6bd60")
base.resizable(False, False)

left_frame_btn_txt = ["Filters", "CLEAR", "btn_3"]
left_frame_btns = []

right_frame_btn_txt = ["Open Image", "Remove image", "Save image", "Undo", "Redo"]
right_frame_btns = []

left_frame = tk.Frame(base, width=590, height=500, bg="#f7ede2")
left_frame.pack(side=tk.LEFT, padx=10, pady=10, fill="both", expand=True)
left_frame.pack_propagate(False)

button_frame1 = tk.Frame(left_frame, width=590, height=50, bg="#f5cac3")
button_frame1.pack(side=tk.TOP, fill="both")

feature_frame = tk.Frame(left_frame, width=590, height=600, bg="#f7ede2")
feature_frame.pack(side=tk.LEFT, fill="both")
feature_frame.pack_propagate(False)

for txt in left_frame_btn_txt:
    button = tk.Button(button_frame1, text=txt)
    left_frame_btns.append(button)
    button.pack(side=tk.LEFT, padx=5, pady=10)

# temp function
def clean_all():
    for w in feature_frame.winfo_children():
        w.destroy()

left_frame_btns[0].config(command = show_feature)
left_frame_btns[1].config(command = clean_all) # temp btn

image_label_width = 580
image_label_height = 450

right_frame = tk.Frame(base, width=590, height=500, bg="#f7ede2")
right_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill="both", expand=True)
right_frame.pack_propagate(False)

button_frame2 = tk.Frame(right_frame, width=590, height=50, bg="#f5cac3")
button_frame2.pack(side=tk.TOP, fill="x")
button_frame2.pack_propagate(False)

# Center the image_label
image_label = tk.Label(right_frame, width=image_label_width, height=image_label_height, bg="lightgray")
image_label.pack(padx=5, pady=40, anchor=tk.CENTER)
image_label.pack_propagate(False)


for txt in right_frame_btn_txt:
    button = tk.Button(button_frame2, text=txt)
    right_frame_btns.append(button)
    button.pack(side=tk.LEFT, padx=5, pady=10)

right_frame_btns[0].config(command = open_image)
right_frame_btns[1].config(command = remove_image)
right_frame_btns[2].config(command = save_image)
right_frame_btns[3].config(command = undo)
right_frame_btns[4].config(command = redo)

base.mainloop()


# MANUAL INPUT
# RESET BUTTON
# zoom in zoom out