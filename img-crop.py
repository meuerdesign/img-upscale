from tkinter import *
from PIL import Image, ImageTk, ImageDraw

# Bild öffnen
image = Image.open("gim.jpg")

# Fenster erstellen
root = Tk()
root.title("Bildausschnitt wählen")

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
        # Berechne die Größe des Rechtecks
        width, height = event.x - start_x, event.y - start_y
        # Begrenze die Größe des Rechtecks
        max_width, max_height = 1600, 1600
        width, height = min(width, max_width), min(height, max_height)
        # Berechne die Koordinaten des Rechtecks
        x, y = start_x + width, start_y + height
        # Zeichne neues Rechteck
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

# Bindungen
canvas.bind("<ButtonPress-1>", on_click)
canvas.bind("<ButtonRelease-1>", on_release)
canvas.bind("<Motion>", on_move)

# Schleife ausführen
root.mainloop()