#%%
import tkinter as tk
import PIL
from PIL import Image, ImageTk

# Create a tk object
firstWindow = tk.Tk()

# Create a text label for the tk window object
label = tk.Label(firstWindow, text="Hello World!", bg='blue')

# Pack the label into the window
#label.pack(padx=20, pady=20)

logo = ImageTk.PhotoImage(Image.open('imageFiles/pythonlogo.jpg'))

# Create a quit button; from what I can tell you can't have both text and an image on a button
button = tk.Button(firstWindow, image=logo, command=firstWindow.quit())

#pack the quit button into the window
button.pack(padx=10, pady=10)

# Display the window
firstWindow.mainloop()



# %%
