import json
import fungsi

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
        fungsi.input_data(nama, berat_laundry, jenis_laundry, jenis_pewangi, jarak)
    elif pro == 2:
        nama = input("Masukkan nama Anda: ")
        fungsi.tampilkan_data(nama)
    elif pro == 3:
        nama = input("Masukkan nama: ")
        fungsi.hapus_data(nama)
    
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