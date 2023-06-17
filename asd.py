import tkinter as tk
from tkinter import *
import json
from tkinter import ttk
from tkinter.messagebox import showinfo
from PIL import ImageTk,Image
from tkinter.messagebox import *
import opsi

window = tk.Tk()
window.title("Login")
window.state('zoomed')
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry("%dx%d" % (screen_width, screen_height))
window.resizable(False, False)

bg = PhotoImage(file='./BAGIAN PERTAMA/username.png')
label = Label(window, image=bg)
label.pack(fill="both", expand=True)

window.mainloop()