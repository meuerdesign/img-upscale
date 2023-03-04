from tkinter import *
from PIL import Image, ImageTk

# Bild öffnen und skalieren
image = Image.open("example.jpg")
width, height = image.size
if width > 1920 or height > 1000:
    ratio = min(1920/width, 1080/height)
    image = image.resize((int(width*ratio), int(height*ratio)), Image.LANCZOS)

# Fenster erstellen und auf Bildschirmgröße skalieren
root = Tk()
root.title("Bildausschnitt wählen")
root.geometry("%dx%d" % (root.winfo_screenwidth(), root.winfo_screenheight()))

# Canvas erstellen und Bild laden
canvas = Canvas(root, width=image.width, height=image.height)
canvas.pack()
image_tk = ImageTk.PhotoImage(image)
canvas.create_image(0, 0, anchor=NW, image=image_tk)

# Variablen initialisieren
drawing = False
start_x = None
start_y = None
rectangle = None

# Funktion für Mausbewegung
def on_move(event):
    global drawing, start_x, start_y, rectangle
    if drawing:
        # Lösche das vorherige Rechteck
        if rectangle is not None:
            canvas.delete(rectangle)
        # Zeichne neues Rechteck
        x, y = event.x, event.y
        rectangle = canvas.create_rectangle(start_x, start_y, x, y, outline='red', width=3)

# Funktion für Mausklick
def on_click(event):
    global drawing, start_x, start_y
    drawing = True
    start_x, start_y = event.x, event.y

# Funktion für Freigabe der Maustaste
def on_release(event):
    global drawing
    drawing = False
    # Zuschneiden und speichern des ausgewählten Bereichs
    bbox = (start_x, start_y, event.x, event.y)
    cropped_image = image.crop(bbox)
    cropped_image.save("cropped.jpg")

# Bindungen
canvas.bind("<ButtonPress-1>", on_click)
canvas.bind("<ButtonRelease-1>", on_release)
canvas.bind("<Motion>", on_move)

# Schleife ausführen
root.mainloop()