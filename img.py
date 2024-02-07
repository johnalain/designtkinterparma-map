import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk

# Create the main window
parent = tk.Tk()
parent.title("Image in Tkinter")

# Load and display an image 
#(replace 'your_logo.png' with the path to your image file)
image = Image.open('circle.jpeg')
image = ImageTk.PhotoImage(image)

# Create a label to display the image
image_label = tk.Label(parent, image=image)
image_label.pack()

# Start the Tkinter event loop
parent.mainloop()