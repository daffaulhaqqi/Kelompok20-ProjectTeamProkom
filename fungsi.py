import json
import datetime
import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
import PIL
from tkinter.messagebox import *

with open("data.json", "r") as f:
    read = json.load(f)
    
class InputData:
    def __init__(self):
        input_window = tk.Toplevel()
        self.nama = tk.StringVar()
        self.berat_laundry = tk.StringVar()
        self.jenis_laundry = tk.StringVar()
        self.jenispewangi = tk.StringVar()
        self.alamat = tk.StringVar()
        self.jarak = tk.StringVar()

        pewangi = ["lavender","jeruk","peppermint","strawberry","vanilla","mango"]
        self.jenispewangi.set(pewangi[0])
        laundry = ["express", "reguler"]
        self.jenis_laundry.set(laundry[0])
            
        input_window.config(width=600,height=400)
        input_window.title("Input Data")
        input_window.geometry("700x400")
        input_window.config(bg="white")

        gambar = PhotoImage(file="./inputdata/judul.png")
        label_gambar = Label(input_window,image=gambar, bg="white").pack(padx=10,pady=10)
                                                                            
        lists = PhotoImage(file="./inputdata/LIST.png")
        label_list = Label(input_window,image=lists, bg="white").place(x=140, y=150)

        frame = Frame(input_window, width= 250, height=400, bg="white")
        frame.place(x= 350, y= 150)

        nama_entry = Entry(frame, width=30, font=('arial'), bg="grey", textvariable=self.nama)
        nama_entry.configure(borderwidth=0, relief="solid", foreground="black", background="#f2f2f2", font=('Arial', 10))
        nama_entry.place(x=10,y=00)

        berat_entry = Entry(frame, width=30, font=('arial'), bg="grey", textvariable=self.berat_laundry, show="")
        berat_entry.configure(borderwidth=0, relief="solid", foreground="black", background="#f2f2f2", font=('Arial', 10))
        berat_entry.place(x =10, y=30 )
            
        jenis_pewangi_option = OptionMenu(frame, self.jenispewangi, *pewangi)
        jenis_pewangi_option.configure(borderwidth=0, relief="solid", foreground="black", background="#f2f2f2", font=('Arial', 10), compound='left')
        jenis_pewangi_option.place(x=10, y= 60)

        jenis_laundry_option = OptionMenu(frame, self.jenis_laundry, *laundry)
        jenis_laundry_option.configure(borderwidth=0, relief="solid", foreground="black", background="#f2f2f2", font=('Arial', 10), compound='left')
        jenis_laundry_option.place(x=10, y= 100)

        alamat_entry = Entry(frame, width=30, font=('arial'), bg="grey", textvariable=self.alamat)
        alamat_entry.configure(borderwidth=0, relief="solid", foreground="black", background="#f2f2f2", font=('Arial', 10))
        alamat_entry.place(x=10,y=140)
            
        jarak_entry = Entry(frame, width=30, font=('arial'), bg="grey", textvariable=self.jarak, show="")
        jarak_entry.configure(borderwidth=0, relief="solid", foreground="black", background="#f2f2f2", font=('Arial', 10))
        jarak_entry.place(x=10,y=170)

        frametom = Frame(input_window, width=130, height=50, bg="white")
        button = PhotoImage(file="./inputdata/submit.png")
        submit = Button(frametom, image=button, bg="white", cursor="hand2", borderwidth=0, highlightthickness=0, command=self.input_data) 
        submit.place(x=0,y=0)
        frametom.place(x=570, y=350)
            
        input_window.mainloop()

    def input_data(self):
        x = read['pewangi']

        jarak = self.jarak.get()
        jarak.replace(",",".")
        jarak = float(jarak)
        koma = self.berat_laundry.get()
        koma.replace(",",".")
        koma = float(koma)

        jenis_pewangi = self.jenispewangi.get()
        tanggal = datetime.datetime.now()
        if jarak <= 3:
            harga_delivery = 0
        elif jarak > 3:
            harga_delivery = (jarak-3)*3000

        if self.jenis_laundry.get() == "reguler":
            waktu_selesai = datetime.datetime.now() + datetime.timedelta(days=3)
            harga_laundry = 3500
        else:
            waktu_selesai = datetime.datetime.now() + datetime.timedelta(hours=12)
            harga_laundry = 5000

        total_biaya = (jarak * harga_laundry) + x[jenis_pewangi] + harga_delivery

        data_pelanggan = {
            "nama": self.nama.get(),
            "berat_laundry": koma,
            "jenis_laundry": self.jenis_laundry.get(),
            "jenis_pewangi": self.jenispewangi.get(),
            "harga_laundry_per_kg": harga_laundry,
            "harga_pewangi" : x[jenis_pewangi],
            "tanggal_laundry" : tanggal.strftime("%Y-%m-%d %H:%M:%S"),
            "jarak" : jarak,
            "harga delivery": harga_delivery,
            "total_biaya": total_biaya,
            "estimasi_waktu_selesai": waktu_selesai.strftime("%Y-%m-%d %H:%M:%S")
        }

        print(json.dumps(data_pelanggan, indent=4))
        with open("data.json", 'r') as f:
            jsondata = f.read()
            data = json.loads(jsondata)
            data["pelanggan"].append(data_pelanggan)
            a = json.dumps(data["pelanggan"], indent=4)
        
        with open("data.json", "w") as f:
            f.write(json.dumps(data, indent=4))
        showinfo(title="Input Data", message="Data Berhasil Dimasukkan!")

class OutputData:
    def __init__(self):         
        self.output_window = tk.Toplevel()
        self.namaout = tk.StringVar()
        self.output_window.geometry("600x425")
        self.output_window.title("Output Data")
        self.output_window.config(bg="white")
        self.output_window.resizable(False, False)

        gambar = tk.PhotoImage(file="./BAGIAN MENAMPILKAN DATA/menampilkan.png")
        label_gambar = tk.Label(self.output_window, image=gambar, bg="white")
        label_gambar.pack(pady=10)

        gambarnama = tk.PhotoImage(file="./BAGIAN MENAMPILKAN DATA/nama.png")
        label_nama = tk.Label(self.output_window, image=gambarnama, bg="white")
        label_nama.place(x=35, y=60)

        self.nama_entry = tk.Entry(self.output_window, width=45, font=('arial'), bg="grey", textvariable=self.namaout)
        self.nama_entry.configure(borderwidth=0, relief="solid", foreground="black", background="#f2f2f2", font=('Arial', 10))
        self.nama_entry.place(x=200,y=65)

        frametom = tk.Frame(self.output_window, width=130, height=50, bg="white")
        button = tk.PhotoImage(file="./BAGIAN MENAMPILKAN DATA/submit.png")
        submit = tk.Button(frametom, image=button, bg="white", cursor="hand2", borderwidth=0, highlightthickness=0, command=self.output) 
        frametom.place(x=450, y=370)
        submit.place(x=0,y=0)

        self.output_window.mainloop()

    def output(self):
        with open("data.json", "r") as f:
            data = json.load(f)
            found = False
        for pelanggan in data["pelanggan"]:
            if pelanggan["nama"] == self.namaout.get():
                namap = pelanggan["nama"]
                tanggal = pelanggan["tanggal_laundry"]
                berat = pelanggan["berat_laundry"]
                jenis = pelanggan["jenis_laundry"]
                pewangi = pelanggan["jenis_pewangi"]
                hargalaundry = pelanggan["harga_laundry_per_kg"]
                hargapewa = pelanggan["harga_pewangi"]
                total = pelanggan["total_biaya"]
                estimasi = pelanggan["estimasi_waktu_selesai"]
                found = True
                break
        else:
            if not found:
                showinfo(title='Output Data', message='Data Tidak Ditemukan!')
        
        # gambar = tk.PhotoImage(file="./BAGIAN MENAMPILKAN DATA/menampilkan.png")
        # label_gambar = tk.Label(self.output_window, image=gambar, bg="white")
        # label_gambar.pack(pady=10)

        # gambarnama = tk.PhotoImage(file="./BAGIAN MENAMPILKAN DATA/nama.png")
        # label_nama = tk.Label(self.output_window, image=gambarnama, bg="white")
        # label_nama.place(x=35, y=60)

        # self.nama_entry = tk.Entry(self.output_window, width=45, font=('arial'), bg="grey", textvariable=self.namaout)
        # self.nama_entry.configure(borderwidth=0, relief="solid", foreground="black", background="#f2f2f2", font=('Arial', 10))
        # self.nama_entry.place(x=200,y=65)


        frame = tk.Frame(self.output_window, bg="#91C5DF")
        frame.pack()

        nama_label = tk.Label(frame, text="Nama: " + namap, justify='left', bg='#91C5DF')
        nama_label.pack(anchor='w')

        tanggal_label = tk.Label(frame, text="Tanggal: " + tanggal, justify='left', bg='#91C5DF')
        tanggal_label.pack(anchor='w')

        berat_label = tk.Label(frame, text="Berat: " + str(berat), justify='left', bg='#91C5DF')
        berat_label.pack(anchor='w')

        jenis_label = tk.Label(frame, text="Jenis: " + jenis, justify='left', bg='#91C5DF')
        jenis_label.pack(anchor='w')

        pewangi_label = tk.Label(frame, text="Pewangi: " + pewangi, justify='left', bg='#91C5DF')
        pewangi_label.pack(anchor='w')

        harga_laundry_label = tk.Label(frame, text="Harga Laundry per Kg: Rp" + str(hargalaundry), justify='left', bg='#91C5DF')
        harga_laundry_label.pack(anchor='w')

        harga_pewangi_label = tk.Label(frame, text="Harga Pewangi: Rp" + str(hargapewa), justify='left', bg='#91C5DF')
        harga_pewangi_label.pack(anchor='w')

        total_label = tk.Label(frame, text="Total Biaya: Rp" + str(total), justify='left', bg='#91C5DF')
        total_label.pack(anchor='w')

        estimasi_label = tk.Label(frame, text="Estimasi Waktu Selesai: " + estimasi, justify='left', bg='#91C5DF')
        estimasi_label.pack(anchor='w')

        self.output_window.update()

class DelData:
    def __init__(self):         
        self.del_window = tk.Toplevel()
        self.namaout = tk.StringVar()
        self.del_window.geometry("600x425")
        self.del_window.title("Input Data")
        self.del_window.config(bg="white")
        self.del_window.resizable(False, False)

        gambar = tk.PhotoImage(file="./BAGIAN MENGHAPUS DATA/menu.png")
        label_gambar = tk.Label(self.del_window, image=gambar, bg="white")
        label_gambar.pack(pady=10)

        gambarnama = tk.PhotoImage(file="./BAGIAN MENGHAPUS DATA/nama1.png")
        label_nama = tk.Label(self.del_window, image=gambarnama, bg="white")
        label_nama.place(x=35, y=60)

        self.nama_entry = tk.Entry(self.del_window, width=45, font=('arial'), bg="grey", textvariable=self.namaout)
        self.nama_entry.configure(borderwidth=0, relief="solid", foreground="black", background="#f2f2f2", font=('Arial', 10))
        self.nama_entry.place(x=200,y=65)

        frametom = tk.Frame(self.del_window, width=130, height=50, bg="white")
        button = tk.PhotoImage(file="./BAGIAN MENGHAPUS DATA/submit.png")
        submit = tk.Button(frametom, image=button, bg="white", cursor="hand2", borderwidth=0, highlightthickness=0, command=self.delete) 
        frametom.place(x=450, y=370)
        submit.place(x=0,y=0)

        self.del_window.mainloop()
    
    def delete(self):
        with open("data.json", "r") as f:
            data = json.load(f)
            found = False
        for pelanggan in data["pelanggan"]:
            if pelanggan["nama"] == self.namaout.get():
                data["pelanggan"].remove(pelanggan)
                a = json.dumps(data["pelanggan"], indent=4)
                with open("data.json", "w") as f:
                    f.write(json.dumps(data, indent=4))
                showinfo(title='Delete Data', message='Data Berhasil Dihapus!')
                found = True
        else:
                if not found:
                    showinfo(title='Delete Data', message='Data Tidak Ditemukan!')