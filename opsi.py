import tkinter as tk
from tkinter import *
import json
import datetime
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter.messagebox import showinfo
from fungsi import *

#State window
with open("data.json", "r") as f:
    read = json.load(f)
def open_input():
    InputData.tampilan_input(self=NONE)

def opsi():
    menuwindow = tk.Tk()
    menuwindow.title("Menu")
    menuwindow.geometry("700x400")
    menuwindow.config(width=600,height=400,bg="white")
    menuwindow.resizable(False, False)

    #gambar menu
    gambar = tk.PhotoImage(file="./BAGIAN MENU/menu.png")
    labelgambar = tk.Label(menuwindow,image=gambar, bg="white")
    labelgambar.place(anchor="center", y=50, x=350)

    tombol1 = PhotoImage(file="./BAGIAN MENU/memasukkan.png")
    tombol2 = PhotoImage(file="./BAGIAN MENU/tampil.png")
    tombol3 = PhotoImage(file="./BAGIAN MENU/hapus.png")

    frame = Frame(menuwindow, width=300, height=300, bg="white")
    frame.place(anchor="center", y=200, x=350)
    button1 = tk.Button(frame, image=tombol1,cursor="hand2",borderwidth=0, highlightthickness=0, bg="white", command= InputData)
    button1.pack(padx=0, pady=10)
    button2 = tk.Button(frame,image=tombol2, cursor="hand2",borderwidth=0, highlightthickness=0, bg="white",command= OutputData)
    button2.pack(padx=0, pady=10)
    button3 = tk.Button(frame, image=tombol3,cursor="hand2",borderwidth=0, highlightthickness=0, bg="white", command= DelData)
    button3.pack(padx=0, pady=10)
    menuwindow.mainloop()