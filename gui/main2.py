import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import messagebox
from rotate import rot

tk_image = ''
pil_image = ''
image_original = ''
label_aspect_ratio = 0

undo_stack = []
redo_stack = []

def handle_rotate(value):
    global pil_image
    if pil_image:
        push_undo(pil_image)
        pil_image = rot(value, pil_image)
        pil_image = resize_image()
        update_display_image()
        redo_stack.clear()  # Clear redo stack after new action
    else:
        show_error("Image not found")

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
    for widgets in feature_frame.winfo_children():
        widgets.destroy()    
    # rotate ui
    tk.Label(feature_frame, text="Rotate").pack(side=tk.LEFT, anchor="n", padx=5, pady=5)
    rotate_left = tk.Button(feature_frame, text="Rotate Left", command=lambda: handle_rotate(90))
    rotate_left.pack(padx=5, pady=5, side=tk.LEFT, anchor='n')
    rotate_right = tk.Button(feature_frame, text="Rotate Right", command=lambda: handle_rotate(-90))
    rotate_right.pack(padx=5, pady=5, side=tk.LEFT, anchor='n')

    # sharpness ui
    tk.Label(feature_frame, text="Sharpness").pack(side=tk.TOP, anchor="w", padx=5, pady=5)

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
base.resizable(False, False)

left_frame_btn_txt = ["Filters", "CLEAR", "btn_3"]
left_frame_btns = []

right_frame_btn_txt = ["Open Image", "Remove image", "Save image", "Undo", "Redo"]
right_frame_btns = []

left_frame = tk.Frame(base, width=590, height=500, bg="lightgray")
left_frame.pack(side=tk.LEFT, padx=10, pady=10, fill="both", expand=True)
left_frame.pack_propagate(False)

button_frame1 = tk.Frame(left_frame, width=590, height=50, bg="white")
button_frame1.pack(side=tk.TOP, fill="both")

feature_frame = tk.Frame(left_frame, width=590, height=600, bg="lightgray")
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

right_frame = tk.Frame(base, width=590, height=500, bg="lightgray")
right_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill="both", expand=True)
right_frame.pack_propagate(False)

button_frame2 = tk.Frame(right_frame, width=590, height=50, bg="white")
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
