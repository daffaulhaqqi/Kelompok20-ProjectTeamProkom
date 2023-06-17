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
    screen_width = 1280
    screen_height = 720
    menuwindow.geometry("%dx%d" % (screen_width, screen_height))
    menuwindow.resizable(False, False)

    #gambar menu
    bg = tk.PhotoImage(file="./BAGIAN MENU/bg.png")
    label = Label(menuwindow, image=bg)
    label.pack(fill="both", expand=True)

    tombol1 = PhotoImage(file="./BAGIAN MENU/memasukkan.png")
    tombol2 = PhotoImage(file="./BAGIAN MENU/tampil.png")
    tombol3 = PhotoImage(file="./BAGIAN MENU/hapus.png")

    button1 = tk.Button(label, image=tombol1,cursor="hand2",borderwidth=0, highlightthickness=0, bg="white", command= InputData)
    button1.place(x=screen_width/2-245, y=screen_height/2.5-100)
    button2 = tk.Button(label,image=tombol2, cursor="hand2",borderwidth=0, highlightthickness=0, bg="white",command= OutputData)
    button2.place(x= screen_width/2-245, y=screen_height/2.5+50)
    button3 = tk.Button(label, image=tombol3,cursor="hand2",borderwidth=0, highlightthickness=0, bg="white", command= DelData)
    button3.place(x= screen_width/2-245, y=screen_height/2.5+200)
    menuwindow.mainloop()

if __name__ == "__main__":
    opsi()