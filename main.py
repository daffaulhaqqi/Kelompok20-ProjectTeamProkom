import tkinter as tk
from tkinter import *
import json
from tkinter import ttk
from tkinter.messagebox import showinfo
from PIL import ImageTk,Image
from tkinter.messagebox import *
import opsi

def login():
    username = usernam.get()
    password = passwor.get()
    with open('data.json', 'r') as r:
        a = json.load(r)
        if username == a["admin"]["username"] and password == a["admin"]["password"]:
            print("dani")
            loginwindow.destroy()
            showinfo(title="Login", message="Login Berhasil")
            opsi.opsi()
        else:
            showwarning(title="Login", message='Username atau Password Salah')

loginwindow = tk.Tk()

#variable yang dibutuhkan
passwor = tk.StringVar()
usernam = tk.StringVar()


loginwindow.title("Login")
loginwindow.state('zoomed')
screen_width = loginwindow.winfo_screenwidth()
screen_height = loginwindow.winfo_screenheight()
loginwindow.geometry("%dx%d" % (screen_width, screen_height))
loginwindow.resizable(False, False)

bg_image = tk.PhotoImage(file='./BAGIAN PERTAMA/username.png')
bg_label = tk.Label(loginwindow, image=bg_image)
bg_label.pack()

#username entry
usernameEntry=Entry(bg_label,width=25,font=('Courier'), textvariable=usernam)
usernameEntry.configure(borderwidth=0, relief="solid", foreground="black")
usernameEntry.place(x=screen_width/2, y=screen_height/2+25, anchor="center")

#password entry
passEntry=Entry(bg_label,width=25,font=('Courier'), textvariable=passwor)
passEntry.configure(borderwidth=0, relief="flat", foreground="black")
passEntry.place(x=screen_width/2, y=screen_height/2+90, anchor="center")

#gambar button
button = PhotoImage(file="./BAGIAN PERTAMA/Button.png")

#button
button1 = tk.Button(bg_label, cursor="hand2", image=button, borderwidth=0, highlightthickness=0, command=login)
button1.place(x=screen_width/2 - 100, y=screen_height/2 + 150)

loginwindow.mainloop()