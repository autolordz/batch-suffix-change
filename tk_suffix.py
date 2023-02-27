# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 18:59:24 2023

@author: Autolordz
"""

import tkinter as tk
import os
from tkinter import filedialog, messagebox
import shutil

def run_button(path0: str, md: str, txt: str):
    """Rename files with a given extension in a given path."""
    for file_path in os.scandir(path0):
        if file_path.name.endswith(f".{md}"):
            new_path = file_path.name.replace(f".{md}", f".{txt}")
            shutil.move(file_path.path, new_path)
            print(f"move {file_path.path} -> {new_path}")

def browse_button():
    """Select a directory using a file dialog."""
    global folder_path
    folder = filedialog.askdirectory()
    folder_path.set(folder)
    print(folder)

def execute_button():
    """Execute files with a given extension in a given path."""
    path = label3.cget("text")
    # check if path is valid
    try:
        run_button(path, entry1.get(),entry2.get())
        messagebox.showinfo("Success", "Files executed successfully")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# create a window
window = tk.Tk()
window.title("文件名后缀批量更改机")
window.geometry("300x300")

# create widgets
folder_path = tk.StringVar(value="这里显示选择后路径")
label1 = tk.Label(window, text="更改前的后缀")
entry1 = tk.Entry(window)
entry1.insert(0, "txt")
label2 = tk.Label(window, text="更改后的后缀")
entry2 = tk.Entry(window)
entry2.insert(0, "md")
label3 = tk.Label(window,textvariable=folder_path)
button_explore = tk.Button(text="选择文件夹", command=browse_button)
button_run = tk.Button(text="执行", command=execute_button)
button_exit = tk.Button(window,text="Exit",command=exit)

# pack widgets
label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
label3.pack()
button_explore.pack()
button_run.pack()
button_exit.pack()

# start main loop
window.mainloop()