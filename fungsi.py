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
        self.input_window = tk.Toplevel()
        self.nama = tk.StringVar()
        self.berat_laundry = tk.DoubleVar()
        self.jenis_laundry = tk.StringVar()
        self.jenispewangi = tk.StringVar()
        self.alamat = tk.StringVar()
        self.jarak = tk.DoubleVar()
        self.jenis_payment = tk.StringVar()
        self.jenis_bank = tk.StringVar()

        pewangi = ["lavender","jeruk","peppermint","strawberry","vanilla","mango"]
        self.jenispewangi.set(pewangi[0])
        laundry = ["express", "reguler"]
        self.jenis_laundry.set(laundry[0])
        payment = ["Cash", "Transfer Bank"]
        self.jenis_payment.set(payment[0])
        bank = ["-","Mandiri", "BCA"]
        self.jenis_bank.set(bank[0])
            
        self.input_window.title("Input Data")
        xw = 1280
        yw = 720
        self.input_window.geometry("%dx%d" % (xw, yw))
        self.input_window.resizable(False, False)

        bg = PhotoImage(file='./inputdata/bg.png')
        label = Label(self.input_window, image=bg)
        label.pack(fill="both", expand=True)

        nama_entry = Entry(self.input_window, width=30, font=('Courier'), bg="grey", textvariable=self.nama)
        nama_entry.configure(borderwidth=0, relief="solid", foreground="black")
        nama_entry.place(x=xw/2,y=yw/2-110)

        berat_entry = Entry(self.input_window, width=30, font=('Courier'), bg="grey", textvariable=self.berat_laundry, show="")
        berat_entry.configure(borderwidth=0, relief="solid", foreground="black")
        berat_entry.place(x =xw/2, y= yw/2-60)
            
        jenis_pewangi_option = OptionMenu(self.input_window, self.jenispewangi, *pewangi)
        jenis_pewangi_option.configure(borderwidth=0, relief="solid", foreground="black")
        jenis_pewangi_option.place(x=xw/2, y=yw/2-10)

        jenis_laundry_option = OptionMenu(self.input_window, self.jenis_laundry, *laundry)
        jenis_laundry_option.configure(borderwidth=0, relief="solid", foreground="black", compound='left')
        jenis_laundry_option.place(x=xw/2, y=yw/2+40)

        alamat_entry = Entry(self.input_window, width=30, font=('Courier'), bg="grey", textvariable=self.alamat)
        alamat_entry.configure(borderwidth=0, relief="solid", foreground="black")
        alamat_entry.place(x=xw/2,y=yw/2+80)
            
        jarak_entry = Entry(self.input_window, width=30, font=('Courier'), bg="grey", textvariable=self.jarak, show="")
        jarak_entry.configure(borderwidth=0, relief="solid", foreground="black")
        jarak_entry.place(x=xw/2,y=yw/2+130)

        jenis_payment_option = OptionMenu(self.input_window, self.jenis_payment, *payment)
        jenis_payment_option.configure(borderwidth=0, relief="solid", foreground="black", compound='left')
        jenis_payment_option.place(x=xw/2, y=yw/2+180)
        
        jenis_bank_option = OptionMenu(self.input_window, self.jenis_bank, *bank)
        jenis_bank_option.configure(borderwidth=0, relief="solid", foreground="black", compound='left')
        jenis_bank_option.place(x=xw/2, y=yw/2+220)

        button = PhotoImage(file="./inputdata/submit.png")
        submit = Button(self.input_window, image=button, bg="white", cursor="hand2", borderwidth=0, highlightthickness=0, command=self.input_data) 
        submit.place(x=xw-250,y=yw-150)
            
        self.input_window.mainloop()

    def input_data(self):
        x = read['pewangi']

        jarak = self.jarak.get()

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
     
        if not jarak:
            showerror("Error", "Jarak Tidak Boleh Kosong!")

        koma = self.berat_laundry.get()
        if not koma:
            showerror("Error", "Berat Laundry Tidak Boleh Kosong!")

        total_biaya = (jarak * harga_laundry) + x[jenis_pewangi] + harga_delivery
        nama = self.nama.get()
        berat = koma,
        jenis = self.jenis_laundry.get()
        pewangi = self.jenispewangi.get()
        alamat = self.alamat.get()
        bank = self.jenis_bank.get()
        pay = self.jenis_payment.get()
        
        if not nama:
            showerror("Error", "Nama tidak boleh kosong")
        if not berat:
            showerror("Error", "Berat tidak boleh kosong")
        if not jenis:
            showerror("Error", "Jenis laundry tidak boleh kosong")
        if not pewangi:
            showerror("Error", "Pewangi tidak boleh kosong")
        if not alamat:
            showerror("Error", "Alamat tidak boleh kosong")
        if not bank:
            showerror("Error", "Bank tidak boleh kosong")
        if not pay:
            showerror("Error", "Jenis pembayaran tidak boleh kosong")

        data_pelanggan = {
            "nama": self.nama.get(),
            "berat_laundry": koma,
            "jenis_laundry": self.jenis_laundry.get(),
            "jenis_pewangi": self.jenispewangi.get(),
            "harga_laundry_per_kg": harga_laundry,
            "harga_pewangi" : x[jenis_pewangi],
            "tanggal_laundry" : tanggal.strftime("%Y-%m-%d %H:%M:%S"),
            "jarak" : jarak,
            "jenis_payment" : self.jenis_payment.get(),
            "jenis_bank" : self.jenis_bank.get(),
            "alamat" : self.alamat.get(),
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
        xw = 1280
        yw = 720
        self.output_window.geometry("%dx%d" % (xw, yw))
        self.output_window.title("Output Data")
        self.output_window.resizable(False, False)

        gambar = tk.PhotoImage(file="./BAGIAN MENAMPILKAN DATA/bg.png")
        self.label = tk.Label(self.output_window, image=gambar)
        self.label.pack(fill="both", expand=True)

        self.nama_entry = tk.Entry(self.label, width=30, font=('Courier'), bg="grey", textvariable=self.namaout)
        self.nama_entry.configure(borderwidth=0, relief="solid", foreground="black")
        self.nama_entry.place(x=xw/2-100,y=yw/4-10)

        button = tk.PhotoImage(file="./BAGIAN MENAMPILKAN DATA/button.png")
        submit = tk.Button(self.label, image=button,bg="white", cursor="hand2", borderwidth=0, highlightthickness=0, command=self.output) 
        submit.place(x=xw/2-50,y=yw/4+50)

        self.output_window.mainloop()

    def output(self):
        xw = 1280
        yw = 720
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
                alamat = pelanggan["alamat"]
                hargapewa = pelanggan["harga_pewangi"]
                pembayaran = pelanggan["jenis_payment"]
                bank = pelanggan["jenis_bank"]
                total = pelanggan["total_biaya"]
                estimasi = pelanggan["estimasi_waktu_selesai"]
                found = True
                break
        else:
            if not found:
                showinfo(title='Output Data', message='Data Tidak Ditemukan!')

        frame = tk.Frame(self.label)
        frame.place(x= xw/2-250, y= yw/2-45)

        nama_label = tk.Label(frame, text="Nama: " + namap, justify='left',  font="Courier")
        nama_label.pack(anchor='w')

        tanggal_label = tk.Label(frame, text="Tanggal: " + tanggal, justify='left', font="Courier")
        tanggal_label.pack(anchor='w')

        berat_label = tk.Label(frame, text="Berat: " + str(berat), justify='left',  font="Courier")
        berat_label.pack(anchor='w')

        jenis_label = tk.Label(frame, text="Jenis: " + jenis, justify='left',  font="Courier")
        jenis_label.pack(anchor='w')

        pewangi_label = tk.Label(frame, text="Pewangi: " + pewangi, justify='left',  font="Courier")
        pewangi_label.pack(anchor='w')

        harga_laundry_label = tk.Label(frame, text="Harga Laundry per Kg: Rp" + str(hargalaundry), justify='left',  font="Courier")
        harga_laundry_label.pack(anchor='w')

        harga_pewangi_label = tk.Label(frame, text="Harga Pewangi: Rp" + str(hargapewa), justify='left',  font="Courier")
        harga_pewangi_label.pack(anchor='w')

        alamat_label = tk.Label(frame, text="Alamat: " + alamat, justify='left', font="Courier")
        alamat_label.pack(anchor='w')

        pembayaran_label = tk.Label(frame, text="Jenis Pembayaran: " + pembayaran, justify='left',  font="Courier")
        pembayaran_label.pack(anchor='w')

        bank_label = tk.Label(frame, text="Jenis Bank: " + bank, justify='left',  font="Courier")
        bank_label.pack(anchor='w')

        total_label = tk.Label(frame, text="Total Biaya: Rp" + str(total), justify='left',  font="Courier")
        total_label.pack(anchor='w')

        estimasi_label = tk.Label(frame, text="Estimasi Waktu Selesai: " + estimasi, justify='left',  font="Courier")
        estimasi_label.pack(anchor='w')

        self.output_window.update()

class DelData:
    def __init__(self):         
        self.del_window = tk.Toplevel()
        self.namaout = tk.StringVar()
        xw = 1280
        yw = 720
        self.del_window.geometry("%dx%d" % (xw, yw))
        self.del_window.title("Input Data")
        self.del_window.config(bg="white")
        self.del_window.resizable(False, False)

        bg = tk.PhotoImage(file="./BAGIAN MENGHAPUS DATA/bg.png")
        self.label = tk.Label(self.del_window, image=bg)
        self.label.pack(fill="both", expand=True)

        self.nama_entry = tk.Entry(self.label, width=30, font=('Courier'), bg="grey", textvariable=self.namaout)
        self.nama_entry.configure(borderwidth=0, relief="solid", foreground="black")
        self.nama_entry.place(x=xw/2-100,y=yw/4+25)

        button = tk.PhotoImage(file="./BAGIAN MENAMPILKAN DATA/button.png")
        submit = tk.Button(self.label, image=button,bg="white", cursor="hand2", borderwidth=0, highlightthickness=0, command=self.delete) 
        submit.place(x=xw/2-50,y=yw/4+90)

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