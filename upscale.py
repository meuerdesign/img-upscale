import tkinter as tk
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
import tensorflow as tf
from tensorflow import keras

# Laden des vortrainierten Modells
model = keras.models.load_model('path/to/pretrained/model')

# Funktion zum Hochladen einer Datei
def upload_image():
    file_path = filedialog.askopenfilename()
    input_image = Image.open(file_path)
    scaled_image = input_image.resize((256, 256))
    scaled_image = keras.preprocessing.image.img_to_array(scaled_image)
    scaled_image /= 255.0
    output_image = model.predict(tf.expand_dims(scaled_image, axis=0))[0]
    output_image = keras.preprocessing.image.array_to_img(output_image)
    output_image.show()

# Erstellen des GUI-Fensters
root = tk.Tk()
root.title("AI-Hochskalierprogramm")

# Erstellen der Schaltfläche zum Hochladen einer Datei
upload_button = tk.Button(root, text="Datei hochladen", command=upload_image)
upload_button.pack()

# Starten des GUI-Loops
root.mainloop()