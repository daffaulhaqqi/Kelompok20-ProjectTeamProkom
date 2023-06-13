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

#configure class
loginwindow.config(width=600,height=400)
loginwindow.title("Login")
loginwindow.geometry("700x400")
loginwindow.config(bg="white")
loginwindow.resizable(False, False)

# Logo
logo = PhotoImage(file=".\BAGIAN PERTAMA\LOGO.png")
label_logo = Label(loginwindow, image=logo, bg= "white").place(x=230, y=-70)

#Username & Password
userpass = Frame(loginwindow, bg="white", width= 300, height=60)
userpass.place(x= 200, y=198)

#gambar tulisan username dan password   
fontusername = PhotoImage(file="./BAGIAN PERTAMA/username.png")
Label(loginwindow, image=fontusername, bg="white").place(x=10, y=150)

#username entry
usernameEntry=Entry(userpass,width=30,font=('Arial'), bg="Grey", textvariable=usernam)
usernameEntry.configure(borderwidth=0, relief="solid", foreground="black", background="#f2f2f2", font=('Arial', 10))
usernameEntry.pack(padx=35,pady=2)

#password entry
passEntry=Entry(userpass,width=30,font=('Arial'), bg="Grey", textvariable=passwor)
passEntry.configure(borderwidth=0, relief="solid", foreground="black", background="#f2f2f2", font=('Arial', 10))
passEntry.pack(padx=35,pady=14)

#gambar button
button = PhotoImage(file="./BAGIAN PERTAMA/tombol.png")
#button
frameButton = Frame(loginwindow, width=100, height=50)
frameButton.place(x=300, y=300)

button1 = tk.Button(frameButton,bg="white", cursor="hand2", image=button, borderwidth=0, highlightthickness=0, command=login)
button1.place(relx=0.5,rely=0.5, anchor="center")

loginwindow.mainloop()