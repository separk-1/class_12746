#%%
import tkinter as tk
# Create a tk window object
firstWindow = tk.Tk()

# Create a text label for the tk window object
label = tk.Label(firstWindow, text="Hello World!") 

# Pack the label into the window
label.pack(padx=20, pady=20) 

# Display the window
# 
firstWindow.mainloop()

# %%
