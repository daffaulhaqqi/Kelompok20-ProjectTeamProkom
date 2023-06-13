import tkinter as tk
from tkinter import *
import json
import datetime

def input_data(nama, berat_laundry, jenis_laundry, jenis_pewangi, jarak):
    harga_pewangi = {
        "lavender": 1000,
        "jeruk": 1500,
        "peppermint": 2000,
        "strawberry": 1800,
        "vanilla": 1200,
        "mango": 1700
        }
    tanggal = datetime.datetime.now()
    if jarak <= 3:
        harga_delivery = 0
    elif jarak > 3:
        harga_delivery = (jarak-3)*3000

    if jenis_laundry == "reguler":
        waktu_selesai = datetime.datetime.now() + datetime.timedelta(days=3)
        harga_laundry = 3500
    else:
        waktu_selesai = datetime.datetime.now() + datetime.timedelta(hours=12)
        harga_laundry = 5000
    total_biaya = (berat_laundry * harga_laundry) + harga_pewangi[jenis_pewangi] + harga_delivery
    data_pelanggan = {
            "nama": nama,
            "berat_laundry": berat_laundry,
            "jenis_laundry": jenis_laundry,
            "jenis_pewangi": jenis_pewangi,
            "harga_laundry_per_kg": harga_laundry,
            "harga_pewangi": harga_pewangi[jenis_pewangi],
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