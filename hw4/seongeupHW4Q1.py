# Seongeun Park / seongeup / 12-746 A1 / Homework 4-1

import tkinter as tk
from tkinter import filedialog
import csv

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        with open(file_path, newline='', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            first_line = next(reader)
            output_label.config(text=', '.join(first_line))

root = tk.Tk()
root.title("CSV File Reader")

open_button = tk.Button(root, text="Open CSV File", command=open_file)
open_button.pack(pady=20)

output_label = tk.Label(root)
output_label.pack(pady=10)

root.mainloop()