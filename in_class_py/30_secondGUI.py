#%%
import tkinter as tk

# Create a tk object
firstWindow = tk.Tk()

# Create a text label for the tk window object
label = tk.Label(firstWindow, text="Hello World!", bg='blue')

# Pack the label into the window
label.pack(padx=20, pady=20)

#Create a quit button
button = tk.Button(firstWindow, text='Quit', command=firstWindow.quit())

#pack the quit button into the window
button.pack(padx=10, pady=10)

# Display the window
firstWindow.mainloop()


# %%
