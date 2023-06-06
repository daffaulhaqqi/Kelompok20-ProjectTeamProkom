import json
import datetime

def input_data(nama, berat_laundry, jenis_laundry, jenis_pewangi, jarak):
    with open("data.json", "r") as f:
        x = json.load(f)
        pewangi = x["pewangi"]
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
    total_biaya = (berat_laundry * harga_laundry) + pewangi[jenis_pewangi] + harga_delivery
    data_pelanggan = {
            "nama": nama,
            "berat_laundry": berat_laundry,
            "jenis_laundry": jenis_laundry,
            "jenis_pewangi": jenis_pewangi,
            "harga_laundry_per_kg": harga_laundry,
            "harga_pewangi" : pewangi[jenis_pewangi],
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


def tampilkan_data(nama):
    with open("data.json", "r") as f:
        data = json.load(f)
        found = False
        for pelanggan in data["pelanggan"]:
            if pelanggan["nama"] == nama:
                print('Nama Pelanggan:', pelanggan["nama"])
                print('Tanggal Laundry:', pelanggan["tanggal_laundry"])
                print('Berat Laundry:', pelanggan["berat_laundry"])
                print('Jenis Laundry:', pelanggan["jenis_laundry"])
                print('Jenis Pewangi:', pelanggan["jenis_pewangi"])
                print('Harga Laundry Per Kg:', pelanggan["harga_laundry_per_kg"])
                print('Harga Pewangi:', pelanggan["harga_pewangi"])
                print('Total Biaya:', pelanggan["total_biaya"])
                print('Estimasi Waktu Selesai: ', pelanggan["estimasi_waktu_selesai"])
                found = True
                break
        else:
            if not found:
                print("Tidak Ada Nama")
def hapus_data(nama):
    with open("data.json", "r") as f:
        data = json.load(f)
        found = False
        for pelanggan in data["pelanggan"]:
            if pelanggan["nama"] == nama:
                data["pelanggan"].remove(pelanggan)
                a = json.dumps(data["pelanggan"], indent=4)
                with open("data.json", "w") as f:
                    f.write(json.dumps(data, indent=4))
                print('Data Dihapus')
                found = True
        else:
                if not found:
                    print("Data tidak ada!")

def main():
    pro = int(input("Pilih Jenis Program (1/2/3)"))
    if pro == 1:
        nama = input("Masukkan nama Anda: ")
        berat_laundry = float(input("Masukkan berat laundry dalam kilogram: "))
        jenis_laundry = input("Pilih jenis laundry (reguler / express): ")
        jenis_pewangi = input("Pilih jenis pewangi (lavender / jeruk / peppermint): ")
        delivery = input('Menggunakan Jasa Antar Atau Tidak: (ya/tidak) ')
        if delivery == 'ya':
            jarak = int(input('Jarak Berapa dalam km '))
        else:
            jarak = 0
        input_data(nama, berat_laundry, jenis_laundry, jenis_pewangi, jarak)
    elif pro == 2:
        nama = input("Masukkan nama Anda: ")
        tampilkan_data(nama)
    elif pro == 3:
        nama = input("Masukkan nama: ")
        hapus_data(nama)
    
def login():
    while True:
        username = input('Masukkan Username: ')
        password = input('Masukkan Password: ')
        with open('data.json', 'r') as r:
            a = json.load(r)
            if username == a["admin"]["username"] and password == a["admin"]["password"]:
                main()
                lag = input('Ingin Melakukan Program Lagi?')
                while True:
                    if lag.lower() == "tidak":
                        exit()
                        break
                    else:
                        main()
                        lag = input('Ingin Melakukan Program Lagi?')
                        
                        
            else:
                print('Username atau Password Salah')


if __name__ == "__main__":
        login()