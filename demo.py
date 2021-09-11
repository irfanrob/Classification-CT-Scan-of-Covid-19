import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from functools import partial
from tkinter.filedialog import askopenfile, askopenfilename
from keras.models import load_model, Model
import cv2
import numpy as np
from keras import backend as K
import time
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import tensorflow as tf
# main window
root = tk.Tk()
root.geometry("720x720") # size of the top_frame
root.title("DEMO TA ALEXNET")

# frame
top_frame = Frame(root, bd = 10)
top_frame.pack()

middle_frame = Frame(root, bd =10)
middle_frame.pack()

bottom_frame = Frame(root, bd = 10)
bottom_frame.pack()

filepathglobal=""
imgs=None
width = 224
height = 224
dsize = (width, height)
model = tf.keras.models.load_model("best_weight_AlexNet.h5")
# software photo
photo = "No_Image_Available.jpg"
photo = ImageTk.PhotoImage(Image.open(photo))
panel=tk.Label(middle_frame,image= photo)
panel.pack()

# select image
def select_image():
    global filepathglobal
    file_path  = askopenfilename()
    filepathglobal = file_path
    image_testing = cv2.imread(file_path, -1)
    image_testing = cv2.cvtColor(image_testing, cv2.COLOR_BGR2RGB)
    image_testing = cv2.resize(image_testing,dsize)
    image_testing = np.array(image_testing)
    image_testing = Image.fromarray((image_testing * 255).astype(np.uint8))
    image_testing = ImageTk.PhotoImage(image_testing)
    panel.config(image=image_testing)
    panel.photo_ref = image_testing


# load image
def load_image():
    global imgs
    imgs = cv2.imread(filepathglobal,-1)
    imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)
    imgs = cv2.resize(imgs,(dsize))
    imgs = np.array(imgs)
    imgs = np.expand_dims(imgs, axis=0)
    print(imgs.shape)

    return

# prediksi
def predict():
    output = model.predict(imgs, 1)
    print(output)
    final_output= output.argmax(axis=1)
    if final_output == 0 :
        result_text = "Covid"
    else:
        result_text = "Normal"
    predictresult.set(result_text)

btn = Button(top_frame, text="Select an image", command=select_image).pack()


btn_load = Button(middle_frame, text='Load Image',  command = load_image).pack()

btn_predict = Button(middle_frame, text='predict', command = predict).pack()

predictresult = StringVar()
predictresult_label = Label(bottom_frame,font=("Courier", 20), height=3, textvariable=predictresult, fg="black").pack()

top_frame.mainloop()
